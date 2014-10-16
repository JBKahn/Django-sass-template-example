from django.db import models


class TestModel(models.Model):
    first_name = models.CharField(max_length=30)


class Todo(models.Model):
	item = models.CharField(max_length=255)
	is_done = models.BooleanField(default=False)