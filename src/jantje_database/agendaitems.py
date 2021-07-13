"""
    Module to maintain agendaitems
"""
from typing import List, Optional, Type
from database import DatabaseSession
from jantje_database_model import AgendaItem
from sqlalchemy.orm.query import Query
from jantje_database import logger
from jantje_database.exceptions import FilterNotValidError


def get_agenda_items(
    flt_id: Optional[int] = None
) -> Optional[List[AgendaItem]]:
    """ Method that retrieves all, or a subset of, the agendaitems in
        the database.

        Parameters
        ----------
        flt_id : Optional[int]
            Filter on a specific user ID.

        Returns
        -------
        List[AgendaItem]
            A list with the resulting agendaitems sorty in descending
            order on DateTime.

        None
            No users are found.
    """

    # Empty data list
    data_list: Optional[Query] = None

    # Get the token
    with DatabaseSession(commit_on_end=False, expire_on_commit=False) \
            as session:
        # First, we get all users
        data_list = session.query(AgendaItem)

        # Now, we can apply the correct filters
        try:
            if flt_id:
                flt_id = int(flt_id)
                data_list = data_list.filter(AgendaItem.id == flt_id)
        except (ValueError, TypeError):
            logger.error(
                f'User id should be of type {int}, not {type(flt_id)}.')
            raise FilterNotValidError(
                f'User id should be of type {int}, not {type(flt_id)}.')

        # Add a sort to the list
        data_list = data_list.order_by(AgendaItem.datetime.desc())

    # Return the token
    if data_list is not None:
        return data_list.all()
    return None
