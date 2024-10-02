""" 
Module that contains 
(1) command line parser
(2) wrapper function that, given the Agrofood_co2_emission.csv, a country, and an 
    emissions column, prints the total emissions in the country.
"""

from argparse import ArgumentParser, Namespace
from pathlib import Path

#new: now inlcudes all available funcitons
from utils import *


def parse_command_line_args() -> Namespace:
    """
    Parse command line arguments

    Returns:
        Namespace: the parsed command line arguments
    """
    parser = ArgumentParser(
#new: now includes all operations
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
#new: added "--operation" argument to argparse that is NOT required
    parser.add_argument(
        "--operation",
        type=str,
        help="The operation to perform on emissions data (sum, mean, standard deviation,  median)",
        required=False,
    )

    args = parser.parse_args()

    return args

#new: added "operation" variable as a string
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
            options: "sum", "mean", "standard deviation", "median"
    """
    rows = get_rows_by_column_value(file_path=csv_path, column_value=country, column_index=country_colm)

#new: function to get array of data points to make operations easier
    data_points = get_data_points(rows,emissions_colm)

#new: variable to store operation result
    op_result = 0

#new: match-case to run different operations
    match operation:
#new: finding total emissions is it's own function called find_sum
        case "sum":
            op_result = find_sum(data_points)
#new: running find_mean
        case "mean":
            op_result = find_mean(data_points)
#new: running find_standard_dev
        case "standard deviation":
            op_result = find_standard_dev(data_points)
#new: running find_median
        case "median":
            op_result = find_median(data_points)
#new: as per assignment instruction, the default is returning sum. commented out is best practice
        case _:
            operation = "sum"
            op_result = find_sum(data_points)
            #raise ValueError("Operation not recognized")
    
#printing desired result with operation
    print(f"In the {csv_path.name} dataset, for country='{country}', the {operation} of values in column {emissions_colm} is {op_result}.")


if __name__ == "__main__":
    args = parse_command_line_args()
    main(
        csv_path=Path(args.file_path),
        country=args.country,
        country_colm=args.country_column,
        emissions_colm=args.emissions_column,
        operation=args.operation
    )
