""" 
Tests for utils.py
"""

import pytest
import numpy as np
import pandas as pd

from src.utils import (
    compute_mean,
    compute_median,
    compute_standard_deviation,
    compute_sum,
    get_colm_vals_as_floats,
    get_rows_by_column_value,
    get_years,
)


class TestGetRowsByColumnValue:
    @staticmethod
    def test_correcly_reads_csv(tmp_path):
        """Check that a properly formatted CSV is processed correctly"""
        # Arrange
        # Create CSV file
        lines = ["colm1,colm2,colm3", "1,2,3", "a,b,c", "d,2,e"]
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("\n".join(lines))

        expected_output = [["1", "2", "3"], ["d", "2", "e"]]

        # Act
        actual_output = get_rows_by_column_value(
            file_path=csv_file, column_value="2", column_index=1
        )
        # Assert
        assert actual_output == expected_output

    @staticmethod
    def test_missing_file():
        """Check that a missing file throws an error"""
        with pytest.raises(
            FileNotFoundError,
            match=r"Could not find file .*. Please provide a valid path",
        ):
            get_rows_by_column_value(file_path="/a/b/nonexistent.csv", column_value=0)


class TestGetColmValsAsFloats:
    @staticmethod
    def test_basic():
        """Check that function works as expected on non-problematic input"""
        # Arrange
        rows = [["1", "2"], ["4", "-5.5"]]
        colm_index = 1
        expected_output = [2, -5.5]
        # Act
        actual_output = get_colm_vals_as_floats(rows=rows, colm_index=colm_index)
        # Assert
        assert actual_output == expected_output

    @staticmethod
    def test_non_float_error():
        """Check that an error is thrown when values not castable to floats are encountered"""
        rows = [["1", "2"], ["a", "b"]]
        colm_index = 1
        with pytest.raises(
            ValueError, match=r"Can not convert .* in column .* to a float"
        ):
            get_colm_vals_as_floats(rows=rows, colm_index=colm_index)


class TestComputeSum:
    @staticmethod
    def test_basic():
        """Check that sum is computed correctly"""
        input = [1, 2, 3]
        assert compute_sum(array=input) == 6


class TestComputeMean:
    @staticmethod
    def test_basic():
        """Check that mean is computed correctly"""
        input = [1, 2, 3]
        assert compute_mean(array=input) == pytest.approx(6 / 3)


class TestComputeMedian:
    @staticmethod
    def test_odd_len():
        """Check that median is computed correctly for odd-lengthed array"""
        input = [1, 2, 3]
        assert compute_median(array=input) == 2

    @staticmethod
    def test_even_len():
        """Check that median is computed correctly for even-lengthed array"""
        input = [1, 2, 3, 4.5]
        assert compute_median(array=input) == pytest.approx((2 + 3) / 2)


class TestComputeStandardDeviation:
    @staticmethod
    def test_basic():
        """Check that standard deviation is computed correctly"""
        input = [1, 2, 3]
        assert compute_standard_deviation(array=input) == pytest.approx(
            0.816496580927726
        )

# New test for new function
class TestGetYears:
    @pytest.fixture
    def mock_csv(self, tmp_path):
        """
        Create a temporary CSV file for testing.
        """
        data = {
            'Year': [1990, 1991, 1992, 1990, 1993, 1991],  # Duplicate years included
            'Value': [100, 200, 300, 150, 250, 350]
        }
        df = pd.DataFrame(data)
        file_path = tmp_path / "test_years.csv"
        df.to_csv(file_path, index=False)
        return str(file_path)

    @staticmethod
    def test_get_years_sorted(mock_csv):
        """
        Test that the function correctly returns a sorted list of unique years
        """
        result = get_years(file_path=mock_csv, year_column_index=0)
        expected = np.array([1990, 1991, 1992, 1993])
        assert np.array_equal(result, expected)

    @staticmethod
    def test_get_years_empty(tmp_path):
        """
        Test that the function correctly returns a ValueError when an empty CSV file is passed
        """
        empty_csv = tmp_path / "empty.csv"
        pd.DataFrame(columns=["Year", "Value"]).to_csv(empty_csv, index=False)
        with pytest.raises(ValueError):
            get_years(file_path=str(empty_csv), year_column_index=0)

    @staticmethod
    def test_index_out_of_bounds(mock_csv):
        """
        Test that the function correctly returns a ValueError when the column index is out of 
        bounds
        """
        with pytest.raises(ValueError):
            get_years(file_path=mock_csv, year_column_index=2)

    @staticmethod
    def test_get_years_non_integer(tmp_path):
        """
        Test that the function correctly returns a ValueError when the column contains incorrect
        data type
        """
        data = {
            'Year': ['1990', '1991', 'NotAYear', '1993'],
            'Value': [100, 200, 300, 250]
        }
        df = pd.DataFrame(data)
        file_path = tmp_path / "non_integer.csv"
        df.to_csv(file_path, index=False)
        with pytest.raises(ValueError):
            get_years(file_path=str(file_path), year_column_index=0)