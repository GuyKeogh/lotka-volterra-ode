from typing import Final


class LotkaVolterraFixedParameters:
    def __init__(
        self,
        growth_rate_prey: float,
        predation_rate: float,
        reproduction_rate_predator: float,
        death_rate_predator: float,
    ):
        if growth_rate_prey < 0:
            raise ValueError(
                f"growth_rate_prey is not positive ({growth_rate_prey} < 0)"
            )
        if predation_rate < 0:
            raise ValueError(f"predation_rate is not positive ({predation_rate} < 0)")
        if reproduction_rate_predator < 0:
            raise ValueError(
                f"reproduction_rate_predator is not positive ({reproduction_rate_predator} < 0)"
            )
        if death_rate_predator < 0:
            raise ValueError(
                f"death_rate_predator is not positive ({death_rate_predator} < 0)"
            )

        self.growth_rate_prey: Final[float] = growth_rate_prey  # \alpha [arb. units]
        self.predation_rate: Final[float] = predation_rate  # \beta [arb. units]
        self.reproduction_rate_predator: Final[
            float
        ] = reproduction_rate_predator  # \delta [arb. units]
        self.death_rate_predator: Final[
            float
        ] = death_rate_predator  # \gamma [arb. units]

class LotkaVolterraNonPeriodicFixedParameters:
    def __init__(
        self,
        growth_rate_prey: float,
        growth_rate_predator: float,
        carrying_capacity_prey: float,
        carrying_capacity_predator: float,
        predator_effect_on_prey_growth: float,
        prey_effect_on_predator_growth: float,
    ):
        self.growth_rate_prey = growth_rate_prey
        self.growth_rate_predator = growth_rate_predator
        self.carrying_capacity_prey = carrying_capacity_prey
        self.carrying_capacity_predator = carrying_capacity_predator
        self.predator_effect_on_prey_growth = predator_effect_on_prey_growth
        self.prey_effect_on_predator_growth = prey_effect_on_predator_growth
