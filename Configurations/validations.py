from django.forms import ValidationError
from Configurations.config import Config
from Configurations.logger import log_error


class Validations:
    def image_validation(self, image):
        configObj = Config()
        retVal = True
        try:
            if not image:
                retVal = False
                raise ValidationError(configObj.IMAGE_VALIDATION_CONFIG['image_empty_error'])
            else:
                extension = image.name.split(".")[-1]
            
            if extension not in configObj.IMAGE_VALIDATION_CONFIG['image_format']:
                retVal = False
                raise ValidationError(configObj.IMAGE_VALIDATION_CONFIG['image_format_error'])
            
            if image.size > configObj.IMAGE_VALIDATION_CONFIG['image_size']:
                retVal = False
                raise ValidationError(configObj.IMAGE_VALIDATION_CONFIG['image_size_error'])

            if image.size > configObj.IMAGE_VALIDATION_CONFIG['image_base_number'] * configObj.IMAGE_VALIDATION_CONFIG['image_x_axis'] * configObj.IMAGE_VALIDATION_CONFIG['image_y_axis']:
                retVal = False
                raise ValidationError(configObj.IMAGE_VALIDATION_CONFIG['image_size_error'])
        except Exception as e:
            log_error.error(f"Not valid image uploaded : {e}")
        return retVal
    