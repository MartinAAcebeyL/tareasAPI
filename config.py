from decouple import config
class Config:
    pass

class Default(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config('coneccion_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Test(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = config('coneccion_DB_TEST')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

configs = {
    'develop':Config,
    'test':Test,
    'default':Default
}