
from django import forms
from Configurations.config import Config
from Configurations.logger import log_error
from Configurations.validations import Validations
from .models import Image



class ImageForm(forms.ModelForm):    
    binary_image = forms.ImageField(label='Image File')
    class Meta:
        model = Image
        fields = ('title', 'description', 'binary_image')

    def validate_image(self):
        try:
            image = self.cleaned_data.get('binary_image')
            validationObj = Validations()
            validationObj.image_validation(image)            
        except Exception as e:
            log_error.error(f"Not valid image : {e}")
        return image
