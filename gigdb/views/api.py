import functools
import json
import re

import flask

from gigdb.controllers import bands_controller


api_blueprint = flask.Blueprint(name='api',
                               import_name=__name__,
                               url_prefix='/api')


@api_blueprint.route('/bands', methods=['GET'])
def get_bands():
    bands = bands_controller.get_bands()
    http_code = 200 if bands else 404
    return flask.make_response(flask.jsonify(bands), http_code)


@api_blueprint.route('/bands', methods=['POST'])
def post_band():
    name = flask.request.form['name']
    bands_controller.create_band(name)
    return flask.Response(status=201)
