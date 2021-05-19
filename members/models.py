from django.db import models

# Create your models here.

import uuid


class Memberarea(models.Model):
    area_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    area_name = models.CharField(max_length=200)

    def __str__(self):
        return self.area_name
