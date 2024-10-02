""" 
Module that contains 
(1) command line parser
(2) wrapper function that, given the Agrofood_co2_emission.csv, a country, and an 
    emissions column, prints the total emissions in the country.
"""

from argparse import ArgumentParser, Namespace
from pathlib import Path

from utils import *


def parse_command_line_args() -> Namespace:
    """
    Parse command line arguments

    Returns:
        Namespace: the parsed command line arguments
    """
    parser = ArgumentParser(
        description=(
            "Given the Agrofood_co2_emission.csv dataset, this script performs operations on a given column for a givencountry. \n"
            "Operations you can perform are: 'sum', 'median', 'mean', 'standard deviation'\n\n"
        )
    )
    parser.add_argument(
        "--country_column",
        type=int,
        help="The index of the country column in the CSV",
        required=True,
    )
    parser.add_argument(
        "--country",
        type=str,
        help="The country whose data you are interested in",
        required=True,
    )
    parser.add_argument(
        "--emissions_column",
        type=int,
        help="The index of the emissions column in the CSV",
        required=True,
    )
    parser.add_argument(
        "--file_path",
        type=str,
        help="The path to the Agrofood_co2_emission.csv",
        required=True,
    )
    parser.add_argument(
        "--operation",
        type=str,
        help="The operation to perform on emissions data (mean, median, standard deviation)",
        required=True,
    )

    args = parser.parse_args()

    return args


def main(csv_path: Path, country: str, country_colm: int, emissions_colm: int, operation: str):
    """
    Workhorse function that:
        (1) gets the rows of a CSV that correspond to the given country
        (2) computes the total emissions from a given column for the given country

    Args:
        csv_path (Path): path to CSV
        country (str): name of the country
        country_colm (int): index of country column in the CSV
        emissions_colm (int): index of the emissions column in the CSV
        operation (str): operation to perform
            options: "sum", "median", "mean", "standard deviation"
    """
    rows = get_rows_by_column_value(file_path=csv_path, column_value=country, column_index=country_colm)

    data_points = get_data_points(rows,emissions_colm)

    match operation:
        case "sum":
            sum_emissions = find_sum(data_points)
            print(f"In the {csv_path.name} dataset, for country='{country}', the {operation} of values in column {emissions_colm} is {sum_emissions}.")
        case "mean":
            mean_emissions = find_mean(data_points)
            print(f"In the {csv_path.name} dataset, for country='{country}', the {operation} of values in column {emissions_colm} is {sum_emissions}.")
        case _:
            raise ValueError("Operation not recognized")


if __name__ == "__main__":
    args = parse_command_line_args()
    main(
        csv_path=Path(args.file_path),
        country=args.country,
        country_colm=args.country_column,
        emissions_colm=args.emissions_column,
        operation=args.operation
    )
