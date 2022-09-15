class Config:
    pass

class Default(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:nmehmj312@localhost/apiTareas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Test(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:nmehmj312@localhost/apiTareas_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

configs = {
    'develop':Config,
    'test':Test,
    'default':Default
}

# APP_ENV = APP_ENV_TESTING
# TESTING = True
# WTF_CSRF_ENABLED = False
