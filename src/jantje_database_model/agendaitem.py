"""
    This module includes the User class which will be used by
    SQLalchemy ORM.
"""
import datetime
import enum
from database import Database
from sqlalchemy import (Column, DateTime, Boolean, Integer, String)


class AgendaItem(Database.base_class):
    """ SQLalchemy agenda table """

    # Mandatory argument for Database objects within SQLAlchemy
    __tablename__ = 'agenda'

    # Database columns for this table
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, nullable=False)
    all_day = Column(Boolean, nullable=False)
    description = Column(String(128), nullable=False)

    def __repr__(self) -> str:
        """ Represents objects of this class. """
        return f'<AgendaItem for "{self.description}" at {self.id}>'
