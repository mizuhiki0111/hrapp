from django.db import models

class Photo(models.Model):

    image = models.ImageField(upload_to='media')

    def return_photo(self):
        return self.image.url
