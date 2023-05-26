

# Load configuration from TOML file
import toml
import logging


class Config:    
    # LOG_FILENAME = "errorlog.log"
    # logging.basicConfig(filename = LOG_FILENAME, level = logging.ERROR)
    # logging.basicConfig(filename = LOG_FILENAME, format='%(levelname)s %(asctime)s [%(filename)s %(funcName)s %(lineno)d]:%(message)s', level=logging.WARNING)
    CONFIG_FILEPATH = "configurations\config.toml"

    with open(CONFIG_FILEPATH, 'r') as f:
        config = toml.load(f)

    DATABASE_CONFIG = config['database']
    IMAGE_VALIDATION_CONFIG = config['image_validation']
    

    # def log_error(self, error_exception, name):
    #     logger = logging.getLogger(name)      
    #     logger.exception('Error occurred ' + str(error_exception))
    #     return logger



