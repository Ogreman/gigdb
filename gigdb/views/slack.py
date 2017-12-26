import functools
import json
import re

import flask


slack_blueprint = flask.Blueprint(name='slack',
                               import_name=__name__,
                               url_prefix='/slack')


def slack_check(func):
    """
    Decorator for locking down slack endpoints to registered apps only
    """
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        if flask.request.form.get('token', '') in slack_blueprint.config['APP_TOKENS'] or slack_blueprint.config['DEBUG']:
            return func(*args, **kwargs)
        print('[access]: failed slack-check test')
        flask.abort(403)
    return wraps


def admin_only(func):
    """
    Decorator for locking down slack endpoints to admins
    """
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        if flask.request.form.get('user_id', '') in slack_blueprint.config['ADMIN_IDS'] or slack_blueprint.config['DEBUG']:
            return func(*args, **kwargs)
        print('[access]: failed admin-only test')
        flask.abort(403)
    return wraps


def not_bots(func):
    """
    Decorator for preventing triggers by bots
    """
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        if 'bot_id' not in flask.request.form:
            return func(*args, **kwargs)
        print('[access]: failed not-bot test')
        flask.abort(403)
    return wraps


@slack_blueprint.route('', methods=['POST'])
@slack_check
def album_count():
    return '', 200
