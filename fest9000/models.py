from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Message(models.Model):
    name = models.CharField(max_length = 32)
    text = models.CharField(max_length = 64, default = 'Cheer up')

    def __str__(self):
        return self.name + ": " + self.text

@python_2_unicode_compatible
class Profile(models.Model):
    prof = models.CharField(max_length = 128)

    def __str__(self):
        return self.porf

@python_2_unicode_compatible
class Sponsor(models.Model):
    name = models.CharField(max_length = 8)

    def __str__(self):
        return self.name
