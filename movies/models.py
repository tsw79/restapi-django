from django.db import models
from lib.utils import LENGTH_OF_ID, gen_uuid

class Movie(models.Model):
  id = models.CharField(max_length=LENGTH_OF_ID, primary_key=True, default=gen_uuid, editable=False)
  title = models.CharField(max_length=100, null=False)
  storyline = models.CharField(max_length=550, null=False)
  genre = models.CharField(max_length=100, null=False)
  release_year = models.IntegerField()
  runtime = models.IntegerField()

  class Meta:
    db_table = "movies"
