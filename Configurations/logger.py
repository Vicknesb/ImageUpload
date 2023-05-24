import logging

def log_error():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    file = logging.FileHandler('errorlog.log')
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s() - %(levelname)s - %(message)s')
    file.setFormatter(formatter)
    logger.addHandler(file)
    return logger