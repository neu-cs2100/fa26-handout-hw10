"""HW10 Question 3 Tests

You only need to add tests for the from_string() alternate constructor of the Date class.
"""

import sys
import pytest
sys.path.append('.')
from src.q3 import Date

class TestDate:
    """Unit tests for the Date class."""

    def test_regular_constructor(self) -> None:
        """Test the regular constructor."""
        date = Date(2021, 1, 1)
        assert date.year == 2021
        assert date.month == 1
        assert date.day == 1

    def test_from_timestamp(self) -> None:
        """Test the from_timestamp alternate constructor."""
        timestamp = 1609459200  # Corresponds to 2021-01-01
        date = Date.from_timestamp(timestamp)
        assert date.year == 2021
        assert date.month == 1
        assert date.day == 1
