"""
Tests for main function
"""

from pathlib import Path

import pytest

from print_fires import main


class TestMain:
    @staticmethod
    def test_sum(tmp_path, capfd):
        """Check that correct message is printed with valid inputs and operation='sum'"""
        # Arrange
        csv_file = tmp_path / "test.csv"
        lines = ["country,colm2,emissions", "USA,2,2", "Canada,2,3", "USA,2,4"]
        csv_file.write_text("\n".join(lines))
        country, country_colm, emissions_colm, operation = "USA", 0, 2, "sum"
        expected_print_message = "In the test.csv dataset, for country='USA', the sum of values in column 2 is 6"
        # Act
        main(
            csv_path=csv_file,
            country=country,
            country_colm=country_colm,
            emissions_colm=emissions_colm,
            operation=operation,
        )
        captured = capfd.readouterr()
        # Assert
        assert expected_print_message in captured.out

    @staticmethod
    def test_mean(tmp_path, capfd):
        """Check that correct message is printed with valid inputs and operation='mean'"""
        # Arrange
        csv_file = tmp_path / "test.csv"
        lines = ["country,colm2,emissions", "USA,2,2", "Canada,2,3", "USA,2,4"]
        csv_file.write_text("\n".join(lines))
        country, country_colm, emissions_colm, operation = "USA", 0, 2, "mean"
        expected_print_message = f"In the test.csv dataset, for country='USA', the mean of values in column 2 is 3"
        # Act
        main(
            csv_path=csv_file,
            country=country,
            country_colm=country_colm,
            emissions_colm=emissions_colm,
            operation=operation,
        )
        captured = capfd.readouterr()
        # Assert
        assert expected_print_message in captured.out
