from django.db import models
from tinymce import models as tinymce_models


class Profile(models.Model):
    fullname = models.CharField(max_length=300)
    description = tinymce_models.HTMLField()
