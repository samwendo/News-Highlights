import os

class Config:
    '''
    General confirguration parent class
    '''

    NEWS_API_BASE_URL = "https://newsapi.org/v2/{}?country=us&apiKey={}"

    NEWS_API_KEY = '7ce9e0d51c1f43199e632e877668be4b'

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}