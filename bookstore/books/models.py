from django.db import models
import uuid


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    external_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    authors = models.ManyToManyField(Author)
    published_year = models.IntegerField(default=0)
    acquired = models.BooleanField()
    thumbnail = models.TextField(max_length=2048)
    year = models.SmallIntegerField()
