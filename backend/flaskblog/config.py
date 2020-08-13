import os


def build_database_url(project: str = os.environ.get('PROJECT_NAME', 'blog')) -> str:
    """
    Build the database url.
    Credentials are built from environmental variables.
    :return: the database url
    """
    username = os.environ.get('POSTGRESQL_USER', 'postgres')
    password = os.environ.get('POSTGRESQL_PASSWORD', 'password')
    host = os.environ.get(f'{project}_POSTGRESQL_SERVICE_HOST'.upper())
    port = os.environ.get(f'{project}_POSTGRESQL_SERVICE_PORT'.upper())
    database = os.environ.get('POSTGRESQL_DB', 'hello_flask_dev')
    return f'postgresql://{username}:{password}@{host}:{port}/{database}'


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'xxx'
    SQLALCHEMY_DATABASE_URI = build_database_url()
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
