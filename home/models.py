from django.db import models


class TestModel(models.Model):
    first_name = models.CharField(max_length=30)
