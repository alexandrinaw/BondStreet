from __future__ import unicode_literals

from django.db import models


class Application(models.Model):
    """Represents the entire application for a given user. This decouples the
    application data with the fact that it is 5 steps, and allows for modifications
    in the future, such as A/B testing a different application flow.

    In practice, maybe it wouldn't make sense to model an entire application in one
    model -- for example, there might be logical groupings that make sense to store
    in separate tables.
    """

    favorite_animal = models.CharField(max_length=50)
    favorite_color = models.CharField(max_length=50)
    favorite_body_part = models.CharField(max_length=100)
    favorite_texture = models.CharField(max_length=100)
    favorite_smell = models.CharField(max_length=200)
    favorite_taste = models.CharField(max_length=50)
    favorite_word = models.CharField(max_length=50)

    last_modified = models.DateTimeField('last modified', auto_now=True)
