from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Adminprofile(models.Model):
    user = models.OneToOneField(
        User, related_name="adminprofile", on_delete=models.CASCADE
    )
    image = models.ImageField(
        default="admin-icon.png", upload_to="admin-profile-pictures"
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)