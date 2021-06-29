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
# ---------------------------------------------------------------------
# Load the configurationdetails
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

# Create a logger for the My REST API package
logger = logging.getLogger(preg.name)

# Create a Flask object
logger.debug('Creating Flask object')
flask_app = Flask(__name__, static_folder='../res/img/')

# Configure Jinja2
jinja_loader = jinja2.FileSystemLoader(searchpath="./")
jinja_env = jinja2.Environment(loader=jinja_loader)


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
            'progress': {
                'trimester': int(round((preg.age_in_days % 93 / 93) * 100, 0)),
                'pregnancy': int(round((preg.age_in_days / 280) * 100, 0))
            }
        },
        'dates': ConfigLoader.config['dates']
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
def avatar() -> Optional[Union[str, Response]]:
    """ Image """
    return flask_app.send_static_file('boss-baby.png')
# ---------------------------------------------------------------------
