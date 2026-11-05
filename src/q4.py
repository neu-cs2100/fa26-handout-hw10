"""HW10 Question 4: Class variables vs. instance variables

A Counter class is provided below. It has a class variable `count` that keeps track of the number
of Counter instances created, and an instance variable `instance_number` that stores the instance
number for each Counter object. I.e., the first Counter instance will be assigned 
`instance_number` 0, the second will be assigned `instance_number` 1, and so on.

Your only task for this question is to write the tests. You do not need to add any code to this
src file.

Keep in mind that you cannot control the order in which the tests are run.
"""

class Counter:
    """
    A counter class that keeps track of the number of Counter instances created.
    """
    count: int = 0  # Class variable to keep track of the number of Counter instances

    def __init__(self) -> None:
        """Increase the number of instances of Counter objects."""
        self._instance_number: int = Counter.count  # Instance variable to store the instance number
        Counter.count += 1  # Increment the class variable count whenever a new instance is created

    @property
    def instance_number(self) -> int:
        """Returns the instance number of the Counter object."""
        return self._instance_number

    @classmethod
    def reset_count(cls) -> None:
        """Resets the class variable count to 0."""
        cls.count = 0
