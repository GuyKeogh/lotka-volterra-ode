from typing import Final

from src.time_series_period import calculate_time_series_period, calculate_time_series_population_lags, calculate_time_series_min_to_max_time, CompletePeriodNotRecorded
import numpy as np
from scipy.integrate import odeint

from src.lotka_volterra import SimulatedPopulations, predator_prey_model_sim, predator_prey_model_non_periodic_sim
from src.lotka_volterra_parameters import LotkaVolterraFixedParameters, LotkaVolterraNonPeriodicFixedParameters
from src.ode_result_plotter import ODEResultPlotter


def non_periodic_sim():
    predator_prey_population_size = [10, 1]  # Arbitrary units
    time = np.linspace(0, 50, num=2000)
    growth_rates: list[float] =                    [1.0 , 1.5 , 1.0 , 1.0 , 1.0 , 1.0 , 1.0]
    reproduction_rate_predators: list[float] =     [0.1 , 0.1 , 0.2 , 0.1 , 0.1 , 0.1 , 0.1]
    prey_carrying_capacities: list[float]    =     [1.0 , 1.0 , 1.0 , 2.0 , 1.0 , 1.0 , 1.0]
    predator_carrying_capacities: list[float] =    [0.5 , 0.5 , 0.5 , 0.5 , 1.0 , 0.5 , 0.5]
    predator_effects_on_prey_growth: list[float] = [-0.3, -0.3, -0.3, -0.3, -0.3, -0.8, -0.3]
    prey_effects_on_predator_growth: list[float] = [0.3 , 0.3 , 0.3 , 0.3 , 0.3 , 0.3,  0.8 ]

    count: int = 0
    for (
        growth_rate_prey,  # \alpha
        reproduction_rate_predator,  # \delta
        carrying_capacity_prey,
        carrying_capacity_predator,
        predator_effect_on_prey_growth,
        prey_effect_on_predator_growth,
    ) in zip(
        growth_rates,
        reproduction_rate_predators,
        prey_carrying_capacities,
        predator_carrying_capacities,
        predator_effects_on_prey_growth,
        prey_effects_on_predator_growth,
    ):
        count += 1
        print("\n-------")
        print(f"Growth rate: {growth_rate_prey}")
        print(f"Reproduction rate predator: {reproduction_rate_predator}")
        print(f"Carrying capacity prey: {carrying_capacity_prey}")
        print(f"Carrying capacity predator: {carrying_capacity_predator}")
        print(f"Predator effect on prey growth: {predator_effect_on_prey_growth}")
        print(f"Prey effect on predator growth: {prey_effect_on_predator_growth}")

        fixed_parameters = LotkaVolterraNonPeriodicFixedParameters(
            growth_rate_prey=growth_rate_prey,
            growth_rate_predator=reproduction_rate_predator,
            carrying_capacity_prey=carrying_capacity_prey,
            carrying_capacity_predator=carrying_capacity_predator,
            predator_effect_on_prey_growth=predator_effect_on_prey_growth,
            prey_effect_on_predator_growth=prey_effect_on_predator_growth,
        )
        result = odeint(
            func=predator_prey_model_non_periodic_sim,
            y0=predator_prey_population_size,
            t=time,
            args=(fixed_parameters,),
        )

        output_results(result=result, count=count, time=time)

def periodic_sim():
    predator_prey_population_size = [10, 1]  # Arbitrary units
    time = np.linspace(0, 50, num=2000)
    growth_rates: list[float] =                [1.0, 1.5, 1.0, 1.0, 1.0]
    predation_rates: list[float] =             [0.5, 0.5, 1.0, 0.5, 0.5]
    reproduction_rate_predators: list[float] = [0.1, 0.1, 0.1, 0.2, 0.1]
    death_rate_predators: list[float] =        [0.5, 0.5, 0.5, 0.5, 0.8]

    count: int = 0
    for (
        growth_rate_prey,  # \alpha
        predation_rate,  # \beta
        reproduction_rate_predator,  # \delta
        death_rate_predator,  # \gamma
    ) in zip(
        growth_rates, predation_rates, reproduction_rate_predators, death_rate_predators
    ):
        count += 1
        print("\n-------")
        print(f"Growth rate: {growth_rate_prey}")
        print(f"Predation rate: {predation_rate}")
        print(f"Predator reproduction rate: {reproduction_rate_predator}")
        print(f"Death rate predator: {death_rate_predator}")

        fixed_parameters = LotkaVolterraFixedParameters(
            growth_rate_prey=growth_rate_prey,
            predation_rate=predation_rate,
            reproduction_rate_predator=reproduction_rate_predator,
            death_rate_predator=death_rate_predator,
        )
        result = odeint(
            func=predator_prey_model_sim,
            y0=predator_prey_population_size,
            t=time,
            args=(fixed_parameters,),
        )

        output_results(result=result, count=count, time=time)

def output_results(result, count: int, time):
    simulated_populations: SimulatedPopulations = SimulatedPopulations(
        prey=result[:, 0], predator=result[:, 1]
    )

    print(f"\nScenario: {count}")
    print(f"Min prey count: {round(min(simulated_populations.prey), 2)}")
    print(f"Max prey count: {round(max(simulated_populations.prey), 2)}")
    try:
        print(f"Prey period: {calculate_time_series_period(population=simulated_populations.prey)}")
    except CompletePeriodNotRecorded:
        print("Prey period: No complete period was found.")

    print(f"Min predator count: {round(min(simulated_populations.predator), 2)}")
    print(f"Max predator count: {round(max(simulated_populations.predator), 2)}")

    try:
        print(f"Predator period: {calculate_time_series_period(population=simulated_populations.predator)}")
    except CompletePeriodNotRecorded:
        print("Predator period: No complete period was found.")

    try:
        print(
            f"Predator-Prey Lag: {calculate_time_series_population_lags(prey=simulated_populations.prey, predators=simulated_populations.predator)}")
    except CompletePeriodNotRecorded:
        print("Predator-Prey Lag: No complete period was found.")

    try:
        print(
            f"Predator min to max time: {calculate_time_series_min_to_max_time(population=simulated_populations.prey)}")
    except CompletePeriodNotRecorded:
        print("Predator min to max time: No complete period was found.")

    result_plotter_obj: ODEResultPlotter = ODEResultPlotter(count=count)
    result_plotter_obj.plot_time_series(
        time=time, simulated_populations=simulated_populations
    )
    result_plotter_obj.plot_phase(simulated_populations=simulated_populations)

if __name__ == "__main__":
    non_periodic_sim()

    """
    requested_periodicity: str = ""
    allowed_values = {"periodic", "non-periodic"}
    while requested_periodicity not in allowed_values:
        requested_periodicity = input("'periodic' or 'non-periodic' solution? Type the required periodicity: ").lower()
        if requested_periodicity not in allowed_values:
            print(f"'{requested_periodicity}' not allowed. Must be 'periodic' or 'non-periodic'. Try again.")
    print(f"Finding {requested_periodicity} solution.")

    if requested_periodicity == "periodic":
        periodic_sim()
    elif requested_periodicity == "non-periodic":
        non_periodic_sim()
    else:
        raise ValueError(f"Unknown requested periodicity '{requested_periodicity}'")
    """