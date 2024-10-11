""" 
Tests for utils.py
"""

import pytest

from src.utils import (
    compute_mean,
    compute_median,
    compute_standard_deviation,
    compute_sum,
    get_colm_vals_as_floats,
    get_rows_by_column_value,
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
