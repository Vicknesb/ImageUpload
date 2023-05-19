from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True)
    binary_image = models.BinaryField(null=True,editable=True)

    def __str__(self):
        return f"{self.title},{self.description},{self.image}"
    
