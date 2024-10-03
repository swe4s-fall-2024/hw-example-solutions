"""
Tests for print_fires.py
"""

import numpy as np
import pytest

from print_fires import get_operation_method, parse_command_line_args


class TestGetOperationMethod:
    @staticmethod
    def test_not_allowed_operation():
        """Check an error is raised when the provided operation isn't recognized"""
        with pytest.raises(
            ValueError, match=r"The provided operation .* is not allowed. .*"
        ):
            get_operation_method(
                operation="mean", allowed_operations_to_method_map={"sum": sum}
            )

    @staticmethod
    def test_allowed_operation():
        """Check that the correct operation is returned with an allowed operation"""
        operator = get_operation_method(
            operation="sum",
            allowed_operations_to_method_map={"sum": sum, "mean": np.mean},
        )
        assert operator.__name__ == "sum"
