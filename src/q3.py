"""HW10 Question 3: Using @classmethod to create an alternative constructor

Implement the from_string alternate constructor below according to the documentation.
The regular constructor is provided, and an additional alternate constructor called
from_timestamp is also provided as an example.

Make sure to write tests for your from_string constructor.
"""
from __future__ import annotations
import datetime

class Date:
    """Stores a date with a year, month, and day."""

    def __init__(self, year: int, month: int, day: int):
        """
        Construct a Date with the given year, month, and day.
        
        Args:
            year : int
                The year of the date
            month : int
                The month of the date
            day : int
                The day of the date
        """
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_timestamp(cls, timestamp: float) -> Date:
        """
        Create Date from Unix timestamp

        Args:
            timestamp : float
                Unix timestamp to convert to a Date
        
        Returns:
            Date : Date
                A new Date (instance of this class) created from the provided timestamp
        """
        dt = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
        return cls(dt.year, dt.month, dt.day)

    @classmethod
    def from_string(cls, date_string: str) -> Date:
        """
        Create Date from string formatted like 'YYYY-MM-DD'
        
        Args:
            date_string : str
                Date in 'YYYY-MM-DD' format
        
        Returns:
            Date : A new Date (instance of this class) created from the provided string
        
        Raises:
            ValueError: If the date_string does not contain two hyphens, or if the year, 
                    month, or day cannot be converted to integers.
        """
