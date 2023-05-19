
from django import forms
from .models import Image



class ImageForm(forms.ModelForm):
    binary_image = forms.ImageField(label='Image File')
    class Meta:
        model = Image
        fields = ('title', 'description', 'binary_image')

