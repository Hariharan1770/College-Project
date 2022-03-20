from django.db import models

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    username = models.CharField(max_length=20, help_text='username')
    password = models.CharField(max_length=20, help_text='password')

