""" 
Module that contains 
(1) command line parser
(2) wrapper function that, given the Agrofood_co2_emission.csv, a country, and an 
    emissions column, prints the total emissions in the country.
"""

from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Callable, Dict

from src.utils import (
    compute_mean,
    compute_median,
    compute_standard_deviation,
    compute_sum,
    get_colm_vals_as_floats,
    get_rows_by_column_value,
)

SUM = "sum"
MEDIAN = "median"
MEAN = "mean"
SD = "standard deviation"
ALLOWED_OPERATIONS_TO_METHOD_MAP = {
    SUM: compute_sum,
    MEDIAN: compute_median,
    MEAN: compute_mean,
    SD: compute_standard_deviation,
}


def parse_command_line_args() -> Namespace:
    """
    Parse command line arguments

    Returns:
        Namespace: the parsed command line arguments
    """
    parser = ArgumentParser(
        description=(
            "Given the Agrofood_co2_emission.csv dataset, this script prints the sum, median, mean, or standard deviation of a "
            "given column for a given country. "
            "It can be used, for example, to determine the total emissions from savanna fires "
            "in the United States of America."
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
        help=(
            "The operation to perform on emissions data. Options: 'sum', 'mean', "
            "'standard deviation', or 'median'. Default is: 'sum'"
        ),
        required=False,
        default="sum",
    )

    args = parser.parse_args()

    return args


def get_operation_method(
    operation: str,
    allowed_operations_to_method_map: Dict = ALLOWED_OPERATIONS_TO_METHOD_MAP,
) -> Callable:
    """
    Check that the given operation is one of the allowed operations and, if it is allowed,
    return the operation's corresponding method
    """
    if operation not in allowed_operations_to_method_map.keys():
        raise ValueError(
            (
                f"The provided operation {operation} is not allowed. "
                f"The allowed operations are {allowed_operations_to_method_map.keys()}"
            )
        )
    return allowed_operations_to_method_map[operation]


def main(
    csv_path: Path, country: str, country_colm: int, emissions_colm: int, operation: str
):
    """
    Workhorse function that:
        (1) gets the rows of a CSV that correspond to the given country
        (2) performs the given operation on the given column for the given country

    Args:
        csv_path (Path): path to CSV
        country (str): name of the country
        country_colm (int): index of country column in the CSV
        emissions_colm (int): index of the emissions column in the CSV
        operation (str): operation to perform
            options: 'sum', 'mean', 'standard deviation', 'median'
    """
    operator = get_operation_method(operation=operation)
    rows = get_rows_by_column_value(
        file_path=csv_path, column_value=country, column_index=country_colm
    )
    data = get_colm_vals_as_floats(rows=rows, colm_index=emissions_colm)
    result = operator(data)
    print(
        f"In the {csv_path.name} dataset, for country='{country}', the {operation} of values in column {emissions_colm} is {result}."
    )


if __name__ == "__main__":
    args = parse_command_line_args()
    main(
        csv_path=Path(args.file_path),
        country=args.country,
        country_colm=args.country_column,
        emissions_colm=args.emissions_column,
        operation=args.operation,
    )
