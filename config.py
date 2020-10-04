import os
class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY=os.environ.get('MOVIE_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:iankoech@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #email configurations
    #We've set-up SMTP server and configure the port to use the gmail SMTP server port 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True#Enables transport layer security to secure the emails
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")




class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:iankoech@localhost/watchlist'
    DEBUG = True

class TestConfig(Config):
    """
    Create a new URI to connect to our database
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ian:iankoech@localhost/watchlist_test'


config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}




    