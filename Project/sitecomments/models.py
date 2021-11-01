from django.db import models
from django.utils import timezone


class SiteComments(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
