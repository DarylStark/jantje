"""
    The dashboard application is 'the webserver' for the application.
"""
# ---------------------------------------------------------------------
# Imports
from flask import Flask, Response, render_template
from typing import Union, Optional
from rich.logging import RichHandler
from config_loader import ConfigLoader
import logging
import jinja2
from pregnancy import Pregnancy
from datetime import date
import random
from jantje_database.agendaitems import get_agenda_items
# ---------------------------------------------------------------------
# Load the settings
if not ConfigLoader.load_settings():
    raise TypeError(
        f'Configuration was not yet loaded.')

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    datefmt="[%X]",
    handlers=[RichHandler()]
)

# Create a Pregnancy object to track the pregnancy
preg = Pregnancy(
    conception_date=ConfigLoader.config['baby']['conception_date'])
preg.name = ConfigLoader.config['baby']['name']

# Sort the dates
ConfigLoader.config['dates'].sort(key=lambda x: x['date'], reverse=True)

# Create a logger for the My REST API package
logger = logging.getLogger(preg.name)

# Create a Flask object
logger.debug('Creating Flask object')
flask_app = Flask(__name__, static_folder='../res/img/')

# Configure Jinja2
jinja_loader = jinja2.FileSystemLoader(searchpath="./")
jinja_env = jinja2.Environment(loader=jinja_loader)


def filter_display_date(value: date, show_year: bool = False) -> str:
    """ Jinja filter that converts a DateTime object to a human
        readable string. Example: 2022-01-27 will be converted to
        1 januari 2022. """

    # List with months in dutch
    months = [
        'januari', 'februari', 'maart', 'april', 'mei', 'juni',
        'juli', 'augustus', 'september', 'oktober', 'november', 'december'
    ]

    rv = f'{value.day} {months[value.month - 1]}'
    if show_year:
        rv += f' {value.year}'
    return rv


# Add filters to Jinja2
jinja_env.filters['display_date'] = filter_display_date


# Add the handlers
@flask_app.route('/', methods=['GET'])
def index() -> Optional[Union[str, Response]]:
    """ Main page of the application """

    # Set a object for the template
    data = {
        'baby': {
            'name': preg.name,
            'weeks': preg.age_in_weeks,
            'days': preg.age_in_days % 7,
            'due': preg.due_date,
            'trimester': preg.trimester,
            'pregnancy_week': preg.week,
            'progress': {
                'trimester': int(round((preg.age_in_days % 93 / 93) * 100, 0)),
                'pregnancy': int(round((preg.age_in_days / 280) * 100, 0))
            }
        },
        'dates': get_agenda_items(),
        'random': random.randint(1, 100) % 2 == 0
    }

    # Render the template
    template = jinja_env.get_template('res/html/index.html')
    return Response(
        template.render(data),
        content_type='text/html; charset=utf-8'
    )


@flask_app.route('/style.css', methods=['GET'])
def style() -> Optional[Union[str, Response]]:
    """ CSS File """
    template = jinja_env.get_template('res/css/style.css')
    return Response(
        template.render(),
        content_type='text/css; charset=utf-8'
    )


@flask_app.route('/script.js', methods=['GET'])
def script() -> Optional[Union[str, Response]]:
    """ JS File """
    template = jinja_env.get_template('res/js/script.js')
    return Response(
        template.render(),
        content_type='text/javascript; charset=utf-8'
    )


@flask_app.route('/boss-baby.png', methods=['GET'])
def avatar_male() -> Optional[Union[str, Response]]:
    """ Image """
    return flask_app.send_static_file('boss-baby.png')


@flask_app.route('/agnes.png', methods=['GET'])
def avatar_female() -> Optional[Union[str, Response]]:
    """ Image """
    return flask_app.send_static_file('agnes.png')
# ---------------------------------------------------------------------
