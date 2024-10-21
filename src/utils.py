""" 
Module containing utility/helper functions to facilitate extracting information from 
Agrofood_co2_emission.csv
"""

import math
from pathlib import Path
from typing import Any, Iterable, List, Dict, Union

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_rows_by_column_value(
    file_path: Path, column_value: str, column_index: int = 0
) -> List[List[Union[str, int, float]]]:
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


'''
New set of functions for plot creation
'''

def get_years(
    file_path: str,
    year_column_index: int
) -> List[int]:
    """
    Reads a CSV file and extracts a sorted list of unique years from the specified column.

    Args:
        file_path (str): The path to the CSV file containing the data.
        year_column_index (int): The index of the column that contains the year values.

    Returns:
        List[int]: A sorted list of unique years extracted from the specified column.
    """

    try:
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Check if the file is empty (no rows and/or no columns)
        if df.empty:
            raise ValueError("The CSV file contains no rows.")

        # Check if the column index is valid
        if year_column_index >= df.shape[1]:
            raise ValueError(f"Invalid column index: {year_column_index}")

        # Convert year column to integers
        df.iloc[:, year_column_index] = pd.to_numeric(df.iloc[:, year_column_index], errors='raise')

        # Get unique, sorted list of years
        years = np.sort(np.unique(df.iloc[:, year_column_index]))

        return years.tolist()

    except pd.errors.EmptyDataError as exc:
        # This handles completely empty files (no columns, no rows)
        raise ValueError("The CSV file is completely empty.") from exc
    except ValueError as exc:
        if str(exc) == "The CSV file contains no rows.":
            raise exc  # Don't re-raise, just let it propagate
        raise ValueError(f"Invalid data in year column or column index: {exc}") from exc


def make_urban_proportion_heatmap(
    urban_prop: Dict[str, List[float]],
    years: List[int]
) -> plt.figure:
    """
    Plots and returns a heatmap of urban population proportions, where each row represents a
    country and each column represents a years.

    Args:
        urban_prop (Dict[str, List[float]]): A dictionary where keys are country names and values
        are lists of urban population proportion for each year.
        years (List[int]): List of years that correspond to the columns of the heatmap.
    
    Returns:
        plt.figure: The matplotlib figure object containing the heatmap.
    """

    # Convert the urban_prop dictionary to a DataFrame, with countries as rows and years as columns
    df = pd.DataFrame(urban_prop, index=years).T

    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(17, 5))

    # Plot the heatmap
    sns.heatmap(
        data=df,
        annot=True,
        annot_kws={"size": 8},
        cmap="YlGnBu",
        cbar=True,
        linewidths=.5,
        ax=ax
    )

    # Set the labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Country')
    ax.set_title('Urban Proportions by Country and Year')

    # Save figure object
    fig.savefig(
        fname='plot_outputs/urban_proportions_heatmap.png',
        dpi=300,
        bbox_inches='tight'
    )

def plot_fires_vs_urban(
    urban_prop: List[float],
    fires: List[float],
    country_name: str
) -> plt.figure:
    """
    Plots a scatter plot of forest fires vs. urban population proportion.

    Args:
        urban_prop (List[float]): List of urban population proportions.
        fires (List[float]): List of forest fires corresponding to the urban proportions.
        country_name (str): Name of country whose information is being plotted.

    Returns:
        plt.Figure: The matplotlib figure object containing the scatter plot.
    """

    sns.set_theme(style="whitegrid")

    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(10, 6))

    scatter = ax.scatter(
        x=urban_prop,
        y=fires,
        c=fires,
        cmap='coolwarm',
        s=100,
        alpha=0.7,
        edgecolor='k'
    )

    # Add a colorbar for the fires amount
    cbar = fig.colorbar(scatter)
    cbar.set_label('Forest Fires')

    # Set labels and title with larger font sizes
    ax.set_xlabel('Urban Population Proportion', fontsize=12)
    ax.set_ylabel('Forest Fires', fontsize=12)
    ax.set_title(f'{country_name}: Forest Fires vs. Urban Population Proportion', fontsize=14)

    # Optional: Add a grid for better readability
    ax.grid(True)

    # Save figure object
    fig.savefig(
        fname=f'plot_outputs/{country_name}_fires_vs_urban.png',
        dpi=300,
        bbox_inches='tight'
    )