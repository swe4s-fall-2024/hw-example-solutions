""" 
Module containing utility/helper functions to facilitate extracting information from 
Agrofood_co2_emission.csv
"""

from pathlib import Path
from typing import List
import statistics


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
                row = line.split(",")
                if row[column_index] == column_value:
                    matching_rows.append(row)

            return matching_rows
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Could not find file {file_path}. Please provide a valid path"
        )

def get_data_points(rows,emissions_colm):
    data_points = []
    for row in rows:
        try:
            data_points.append(float(row[emissions_colm]))
        except ValueError:
            raise ValueError(
                f"Can not convert {row[emissions_colm]} in column {emissions_colm} to a float"
            )
    return data_points
   
def find_sum(data_points):
    total_emissions = 0
    for point in data_points:
        total_emissions += point
    return total_emissions

def find_mean(data_points):
    mean_emissions = statistics.mean(data_points)
    return mean_emissions

def find_standard_dev(data_points):

    return

def find_median(data_points):
    return