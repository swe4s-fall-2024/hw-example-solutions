import os
import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.parser_utils import ArgsFormatter
from src.utils import (
    get_rows_by_column_value,
    get_years,
    make_urban_proportion_heatmap,
    plot_fires_vs_urban,
)


def parse_command_line_args() -> Namespace:

    parser = ArgumentParser(
        description=(
            "Given the Agrofood_co2_emission.csv dataset, this script generates plots based on the data provided."
        ),
    )
    parser.add_argument(
        "-l",
        "--countries_list",
        type=str,
        nargs="+",
        help="List of countries to make plots for",
        required=True,
    )
    parser.add_argument(
        "-n",
        "--country_column",
        type=str,
        help="Column index corresponding to the country names",
        required=True,
    )
    parser.add_argument(
        "-y",
        "--year_column",
        type=str,
        help="Column index corresponding to year",
        required=True,
    )
    parser.add_argument(
        "-r",
        "--rural_column",
        type=str,
        help="Column index corresponding to rural population",
        required=True,
    )
    parser.add_argument(
        "-u",
        "--urban_column",
        type=str,
        help="Column index corresponding to urban population.",
        required=True,
    )
    parser.add_argument(
        "-t",
        "--forest_fire_column",
        type=str,
        help="Column index corresponding to forest fires.",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--file_path",
        type=str,
        help="Path to the CSV file containing the emissions data.",
        required=True,
    )

    args = parser.parse_args()

    return args


def main(
    csv_path: Path,
    countries: str,
    country_colm: str,
    year_colm: str,
    rural_colm: str,
    urban_colm: str,
    fires_colm: str,
):
    # Get the years to plot
    years = get_years(file_path=csv_path, year_column_index=int(year_colm))

    # For each country, store the urban/total proportion AND forest fires for each year
    urban_prop = {}
    forest_fires = {}

    for country in countries:
        country_df = pd.DataFrame(
            get_rows_by_column_value(
                file_path=csv_path, column_value=country, column_index=int(country_colm)
            )
        )

        # Calculate urban population proportion
        props = pd.to_numeric(country_df.iloc[:, int(urban_colm)], errors="coerce") / (
            pd.to_numeric(country_df.iloc[:, int(urban_colm)], errors="coerce")
            + pd.to_numeric(country_df.iloc[:, int(urban_colm)], errors="coerce")
        )

        # Store the proportions in the dictionary
        urban_prop[country] = props.tolist()
        forest_fires[country] = country_df.iloc[:, int(fires_colm)].tolist()

    # Make and save urban population proportion heatmap
    make_urban_proportion_heatmap(urban_prop=urban_prop, years=years)

    # Plot urban proportion vs. forest fires for each country
    for country in countries:
        plot_fires_vs_urban(
            urban_prop=pd.to_numeric(urban_prop[country]),
            fires=pd.to_numeric(forest_fires[country]),
            country_name=country,
        )


if __name__ == "__main__":
    args = parse_command_line_args()
    main(
        csv_path=Path(args.file_path),
        countries=args.countries_list,
        country_colm=args.country_column,
        year_colm=args.year_column,
        rural_colm=args.rural_column,
        urban_colm=args.urban_column,
        fires_colm=args.forest_fire_column,
    )
