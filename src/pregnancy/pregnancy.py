"""
    Module that contains the static 'Pregnancy' class.
"""
# ---------------------------------------------------------------------
# Imports
from typing import Optional
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
        """ Returns the trimester you're in now. """
        return int((self.percentage // 33.3333) + 1)

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
