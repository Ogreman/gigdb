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
