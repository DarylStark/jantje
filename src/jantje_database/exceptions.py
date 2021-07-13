"""
    Exceptions for the 'jantje_database' package.
"""


class JantjeDatabaseError(Exception):
    """ Base exception for MyDatabase-exceptions. """
    pass


class FilterNotValidError(JantjeDatabaseError):
    """ Exception that occurs when the user tries to filter on a wrong
        type. """
    pass


class ConfigNotLoadedError(JantjeDatabaseError):
    """ Exception when the configuration couldn't be loaded. """
    pass
