class Config:
    SECRET_kEY = '123'

class Default(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:nmehmj312@localhost/apiTareas'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

configs = {
    'develop':Config,
    'default':Default
}