import tomllib
from django import forms
from .models import Image
from django.core.exceptions import ValidationError
configpath = 'config.toml'


class ImageForm(forms.ModelForm):
    binary_image = forms.ImageField(label='Image File')
    class Meta:
        model = Image
        fields = ('title', 'description', 'binary_image')

    def clean_binaryimage(self):
        image = self.cleaned_data.get('binary_image')
        with open(configpath, 'rb') as f:
            data = tomllib.load(f)
            image_size = data.get('image_validation')['image_size']
            image_format = data.get('image_validation')['image_format']
            image_size_error = data.get('image_validation')['image_size_error']
            image_format_error = data.get('image_validation')['image_format_error']
            image_empty_error = data.get('image_validation')['image_empty_error']

            if not image:
                raise ValidationError(image_empty_error)
            else:
                extension = image.name.split(".")[-1]
            if extension not in image_format:
                raise ValidationError(image_format_error)
            if image:
                if image.size > image_size:
                    raise ValidationError(image_size_error)

        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError(image_size_error)
            return image
