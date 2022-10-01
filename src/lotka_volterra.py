from dataclasses import dataclass

from src.lotka_volterra_parameters import LotkaVolterraFixedParameters, LotkaVolterraNonPeriodicFixedParameters


def predator_prey_model_sim(
    prey_predator_population_sizes: tuple[float, float],
    time,
    fixed_parameters: LotkaVolterraFixedParameters,
) -> tuple[float, float]:
    population_size_prey, population_size_predator = prey_predator_population_sizes

    rate_of_change_of_prey = (
        fixed_parameters.growth_rate_prey * population_size_prey
        - fixed_parameters.predation_rate
        * population_size_prey
        * population_size_predator
    )
    rate_of_change_of_predator = (
        fixed_parameters.reproduction_rate_predator
        * population_size_prey
        * population_size_predator
        - fixed_parameters.death_rate_predator * population_size_predator
    )

    return rate_of_change_of_prey, rate_of_change_of_predator

def predator_prey_model_non_periodic_sim(
    prey_predator_population_sizes: tuple[float, float],
    time,
    fixed_parameters: LotkaVolterraNonPeriodicFixedParameters,
) -> tuple[float, float]:
    population_size_prey, population_size_predator = prey_predator_population_sizes

    rate_of_change_of_prey = (
        (fixed_parameters.growth_rate_prey * population_size_prey) * (
            (fixed_parameters.carrying_capacity_prey - population_size_prey
            - fixed_parameters.predator_effect_on_prey_growth * population_size_predator)/fixed_parameters.carrying_capacity_prey
        )
    )
    rate_of_change_of_predator = (
        (fixed_parameters.growth_rate_predator * population_size_predator) * (
        (fixed_parameters.carrying_capacity_predator - population_size_predator
         - fixed_parameters.prey_effect_on_predator_growth * population_size_prey) / fixed_parameters.carrying_capacity_predator
        )
    )

    return rate_of_change_of_prey, rate_of_change_of_predator


@dataclass(frozen=True)
class SimulatedPopulations:
    prey: tuple[float]
    predator: tuple[float]
