class Config(object):
    """
    Common configurations
    """


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    #FLASK
    FLASK_DEBUG = True
    #SQL ALCHEMY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/mutants.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class QualityConfig(Config):
    """
    QA Ambient configurations
    """
    #FLASK
    FLASK_DEBUG = True
    #SQL ALCHEMY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/mutants.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    #FLASK
    FLASK_DEBUG = True
    #SQL ALCHEMY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/mutants.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    


app_config = {
    'dev': DevelopmentConfig,
    'qa':QualityConfig,
    'pro': ProductionConfig
}