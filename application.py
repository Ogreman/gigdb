from gigdb.setup import create_app, db  # NOQA
application = create_app()


@application.shell_context_processor
def make_shell_context():
    from gigdb.models.bands import Band
    return {'db': db, 'Band': Band}