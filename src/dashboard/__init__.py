"""
    The dashboard application is 'the webserver' for the application.
"""
# ---------------------------------------------------------------------
# Imports
from flask import Flask, Response, render_template
from typing import Union, Optional
from rich.logging import RichHandler
import logging
import jinja2
# ---------------------------------------------------------------------
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    datefmt="[%X]",
    handlers=[RichHandler()]
)

# Create a logger for the My REST API package
logger = logging.getLogger('Jantje')

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
    template = jinja_env.get_template('res/html/index.html')
    return Response(
        template.render(),
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
