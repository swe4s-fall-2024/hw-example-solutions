""" 
Module containing utility/helper functions to facilitate extracting information from 
Agrofood_co2_emission.csv
"""

import math
from pathlib import Path
from typing import Any, Iterable, List

import numpy as np


def get_rows_by_column_value(
    file_path: Path, column_value: str, column_index: int = 0
) -> List[List[str]]:
    """
    Read assumed CSV file line-by-line. Split each line by "," into a list of strings.
    Calling each line's list of strings 'row', return those rows for which
    row[colum_index] == column_value.

    Args:
        file_path (Path): path to CSV
        column_value (str): query value
        column_index (int, optional): index of column to query on. Defaults to 0.

    Returns:
        List[List[str]]: rows for which row[colum_index] == column_value.
    """
    try:
        with open(file_path, "r") as file:
            matching_rows = []
            for line in file:
                row = line.strip().split(",")
                if row[column_index] == column_value:
                    matching_rows.append(row)

            return matching_rows
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Could not find file {file_path}. Please provide a valid path"
        )


def get_colm_vals_as_floats(
    rows: Iterable[Iterable[Any]], colm_index: int
) -> List[float]:
    """
    Given a list rows=[r1, r2, ... ] of lists and an index i, return
    [float(r1[i]), float(r2[i]), ...]

    Args:
        rows (List[Any]): list of lists where each sublist represents a row of some dataset
        colm_index (int): index of column to select

    Raises:
        ValueError: _description_

    Returns:
        List[float]: [float(r1[i]), float(r2[i]), ...] where rows=[r1, r2, ...]
    """
    out_array = []
    for row in rows:
        try:
            out_array.append(float(row[colm_index]))
        except ValueError:
            raise ValueError(
                f"Can not convert {row[colm_index]} in column {colm_index} to a float"
            )
    return out_array


def compute_sum(array: Iterable[float]) -> float:
    total = 0
    for val in array:
        total += val
    return total


def compute_mean(array: Iterable[float]) -> float:
    total = compute_sum(array=array)
    return total / len(array)


def compute_standard_deviation(array: Iterable[float]) -> float:
    mean = compute_mean(array=array)
    sum_squared_residuals = 0
    for val in array:
        sum_squared_residuals += (val - mean) ** 2
    return np.sqrt((1 / len(array)) * sum_squared_residuals)


def compute_median(array: Iterable[float]) -> float:
    sorted_array = sorted(array)
    if len(array) % 2 == 0:
        # handle even-length array
        left_index = int(len(array) / 2) - 1
        return (array[left_index] + array[left_index + 1]) / 2

    # handle odd-length array
    return array[math.floor(len(array) / 2)]
