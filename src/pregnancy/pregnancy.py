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


if __name__ == '__main__':
    console = Console()

    # Initialize the baby
    jantje = Baby(conception_date='2021-04-22')
    jantje.name = 'Jantje'

    # Print progress
    console.print(f'\n[u][b]{jantje.name}[/b][/u]\n')
    console.print(f'Progress:   {jantje.age}')
    console.print(f'Percentage: {round(jantje.percentage, 2)}%')
    console.print(f'Trimester:  {jantje.trimester}')
    console.print(f'Due date:   {jantje.due_date}')
    console.print(f'Days left:  {jantje.days_till_due_date}')

    console.print('\n[u][b]Progress trackers:[/b][/u]\n')

    with Progress(expand=True, console=console) as progress:
        complete = progress.add_task('[green]Pregnancy', total=(40 * 7))
        progress.update(complete, advance=jantje.age_in_days)

    with Progress(expand=True, console=console) as trimester:
        complete = trimester.add_task('[green]Trimester', total=(93))
        trimester.update(complete, advance=(jantje.age_in_days % 93))

    console.print()
