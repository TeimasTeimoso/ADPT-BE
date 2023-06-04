import logging

def configure_logger(environment: str) -> logging.Logger:
    if environment == 'dev':
        logging.basicConfig(level=logging.DEBUG)
    elif environment == 'prod':
        logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w')

    return logging.getLogger(__name__)