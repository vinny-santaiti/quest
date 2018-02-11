class Config(object):
    DEBUG = False
    DATABASE_URI = 'sqlite://:memory:'

class ProdConfig(Config):
    DATABASE_URI = 'postgres://user@localhost/foo'

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True
