import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'change-me')
    APP_TOKENS = [
        token for key, token in os.environ.items()
        if key.startswith('APP_TOKEN')
    ]
    ADMIN_IDS = [
        user_id for key, user_id in os.environ.items()
        if key.startswith('ADMIN_ID')
    ]
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI",
                                        "postgres://postgres:postgres@localhost:5432/postgres")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # This handles session rollback on exception and commit on success,
    # https://github.com/mitsuhiko/flask-sqlalchemy/pull/115/files


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
