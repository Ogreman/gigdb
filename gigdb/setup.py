import os
from pathlib import Path

import flask


def add_blueprints(application):
    # from gigdb.views.api import api_blueprint
    # application.register_blueprint(api_blueprint)
    # api_blueprint.config = application.config.copy()

    # from gigdb.views.site import site_blueprint
    # application.register_blueprint(site_blueprint)
    # site_blueprint.config = application.config.copy()

    from gigdb.views.slack import slack_blueprint
    application.register_blueprint(slack_blueprint)
    slack_blueprint.config = application.config.copy()


def create_app():
    TEMPLATE_DIR = Path(__file__).parent.joinpath('templates')
    
    app = flask.Flask(__name__, template_folder=TEMPLATE_DIR)
    app.config.from_object(os.environ['APP_SETTINGS'])

    add_blueprints(app)

    return app
