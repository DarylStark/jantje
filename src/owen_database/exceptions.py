"""
    Exceptions for the 'owen_database' package.
"""


class OwenDatabaseError(Exception):
    """ Base exception for MyDatabase-exceptions. """
    pass


class FilterNotValidError(OwenDatabaseError):
    """ Exception that occurs when the user tries to filter on a wrong
        type. """
    pass


class ConfigNotLoadedError(OwenDatabaseError):
    """ Exception when the configuration couldn't be loaded. """
    pass
