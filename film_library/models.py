from django.db import models
from django.utils import timezone


class User(models.Model):
    login = models.CharField(max_length=15)
    created_date = models.DateTimeField(timezone.now())

    def publish(self):
        self.save()

    def __str__(self):
        return self.login
