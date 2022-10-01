import numpy as np
from typing import Final

class CompletePeriodNotRecorded(Exception):
    pass


def calculate_time_series_period(population: tuple[float]) -> int:
    decimal_places: Final[int] = 2  # Rounding required to overcome floating point precision errors
    min_time_difference: Final[int] = 10  # Prevent points from same peak being used

    population_floored: list[float] = list(((population * 10 ** decimal_places) // 1) / (10 ** decimal_places))
    population_maximums: list[int] = np.where(population_floored == max(population_floored))[0].tolist()
    if len(population_maximums) > 1:
        time_difference = population_maximums[1] - population_maximums[0]
        if time_difference > min_time_difference:
            return time_difference
        else:
            for time in population_maximums:
                time_difference = time - population_maximums[0]
                if time_difference > min_time_difference:
                    return time_difference

    raise CompletePeriodNotRecorded

def calculate_time_series_min_to_max_time(population: tuple[float]) -> int:
    decimal_places: Final[int] = 2  # Rounding required to overcome floating point precision errors
    min_time_difference: Final[int] = 10  # Prevent points from same peak being used

    population_floored: list[float] = list(((population * 10 ** decimal_places) // 1) / (10 ** decimal_places))
    population_maximums: list[int] = np.where(population_floored == max(population_floored))[0].tolist()
    population_minimums: list[int] = np.where(population_floored == min(population_floored))[0].tolist()
    if len(population_maximums) > 1:
        time_difference = population_minimums[0] - population_maximums[0]
        if time_difference > min_time_difference:
            return time_difference
        else:
            for time in population_minimums:
                time_difference = time - population_maximums[0]
                if time_difference > min_time_difference:
                    return time_difference

    raise CompletePeriodNotRecorded

def calculate_time_series_population_lags(prey: tuple[float], predators: tuple[float]) -> int:
    decimal_places: Final[int] = 2  # Rounding required to overcome floating point precision errors
    min_time_difference: Final[int] = 10  # Prevent points from same peak being used

    prey_floored: list[float] = list(((prey * 10 ** decimal_places) // 1) / (10 ** decimal_places))
    prey_maximums: list[int] = np.where(prey_floored == max(prey_floored))[0].tolist()

    predators_floored: list[float] = list(((predators * 10 ** decimal_places) // 1) / (10 ** decimal_places))
    predators_maximums: list[int] = np.where(predators_floored == max(predators_floored))[0].tolist()

    if len(prey_maximums) > 1:
        time_difference = predators_maximums[0] - prey_maximums[0]
        if time_difference > min_time_difference:
            return time_difference
        else:
            for time in predators_maximums:
                time_difference = time - prey_maximums[0]
                if time_difference > min_time_difference:
                    return time_difference

    raise CompletePeriodNotRecorded
