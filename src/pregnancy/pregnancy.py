"""
    Module that contains the static 'Pregnancy' class.
"""
# ---------------------------------------------------------------------
# Imports
from typing import Optional, Tuple
from datetime import datetime
from datetime import date
from datetime import timedelta
from rich.console import Console
from rich.progress import Progress
# ---------------------------------------------------------------------


class Pregnancy:
    """ Class that represents a pregnancy """

    def __init__(self, conception_date: str) -> None:
        """ Sets the default values """
        self.conception = conception_date
        self.conception_date = datetime.strptime(
            self.conception, '%Y-%m-%d').date()
        self.name = None

    @property
    def age_in_days(self) -> int:
        """ Returns the progress of the pregnancy in days. """
        return (date.today() - self.conception_date).days

    @property
    def age_in_weeks(self) -> int:
        """ Returns the progress of the pregnancy in weeks. """
        return (date.today() - self.conception_date).days // 7

    @property
    def age(self) -> str:
        """ Returns the progress of the pregnancy in a human readable
            format. """
        return f'{self.age_in_weeks} weeks and {self.age_in_days % 7} days'

    @property
    def percentage(self) -> float:
        """ Returns the procentage of the pregnancy. """
        return (self.age_in_days / (40 * 7)) * 100

    @property
    def trimester(self) -> int:
        """ Returns the trimester you're in now. The pregnancy is
            divided as follows:

            Trimester 1: week 0 - 12
            Trimester 2: week 13 - 26
            Trimester 3: week 26 and onwards
        """
        if self.age_in_weeks <= 12:
            return 1
        if self.age_in_weeks <= 26:
            return 2
        return 3

    @property
    def trimester_days(self) -> Tuple[int, int]:
        """ Returns the amount of days that you're in the trimester and
            the number of days in this trimester. It assumes that the
            third trimester takes till week 40 """

        # Get the trimester
        trimester = self.trimester

        # Calculate the days before the trimester
        days_before = (trimester - 1) * 7 * 12

        # Get the days within this trimester
        try:
            trimester_length = (7 * 12, 7 * 12, 7 * 16)[trimester - 1]
        except IndexError:
            return (-1, -1)

        # Get the length of the current trimester
        length = self.age_in_days - days_before

        # Return the value
        return (length, trimester_length)

    @property
    def due_date(self) -> date:
        """ Returns the due date. """
        return self.conception_date + timedelta(days=280)

    @property
    def days_till_due_date(self) -> int:
        """ Returns the days till due date. """
        return (self.due_date - date.today()).days

    @property
    def week(self) -> int:
        """ Returns in which week of the pregnancy you are. """
        return self.age_in_weeks + 1
# ---------------------------------------------------------------------
