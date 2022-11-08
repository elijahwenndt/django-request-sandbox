from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=300)
    published_year = models.IntegerField(null=True, blank=True)