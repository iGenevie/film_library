from django.db import models
from django.utils import timezone


class User(models.Model):
    login = models.CharField(max_length=15)
    created_date = models.DateTimeField(timezone.now())

    def publish(self):
        self.save()

    def __str__(self):
        return self.login


class Film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_title = models.CharField(max_length=20)
    production = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    year = models.IntegerField()
    added_date = models.DateTimeField(timezone.now())

    def publish(self):
        self.save()

    def __str__(self):
        return self.original_title
