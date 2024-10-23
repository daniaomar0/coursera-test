from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')
    first_time_login = models.BooleanField(default=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.first_name} Profile'

    def save(self, *args, **kwargs):
      super().save(*args, **kwargs)

    # Ensure the image exists before opening it
      if self.image:
        img = Image.open(self.image.path)

        # Resize the image if it's larger than 300x300
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
