

# Load configuration from TOML file
import toml


with open('config.toml', 'r') as f:
    config = toml.load(f)

DATABASE_CONFIG = config['database']
IMAGE_VALIDATION_CONFIG = config['image_validation']
MODEL_PROPS_CONFIG = config['model_name']

