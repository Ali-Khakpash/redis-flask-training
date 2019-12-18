import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
   SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
   SQLALCHEMY_COMMIT_ON_TEARDOWN = True
   FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
   FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
   FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

   @staticmethod
   def init_app(app):
       pass

class DevelopmentConfig(Config):
      DEBUG = True
      REDIS_URL = 'redis://localhost:6379/0'


class TestingConfig(Config):
      TESTING = True
      SQLALCHEMY_DATABASE_URI = ''

class ProductionConfig(Config):
      SQLALCHEMY_DATABASE_URI = ''

config = {






































































































    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}