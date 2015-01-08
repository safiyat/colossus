#Settings

class Base(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'the-secret-key-is-here'


class Development(Base):
    DEBUG = True
    TESTING = False
    MONGODB_SETTINGS = {
        'DB': 'colossus', 
        'host': 'localhost', 
        'port': 27017,
    }


class Testing(Base):
    pass

class Staging(Base):
    pass

class Production(Base):
    pass
