class Config(object):
    WTF_CSRF_ENABLED=False
    MAIL_SERVER=""
    MAIL_USERNAME=""
    MAIL_PASSWORD=""

class DevelopmentConfig(Config):
    DEBUG=True
    LOG_LOCATION="./log.log"

class ProductionConfig(Config):
    DEBUG=False
    LOG_LOCATION="/var/log/pysites/{{cookiecutter.repo_name}}"
