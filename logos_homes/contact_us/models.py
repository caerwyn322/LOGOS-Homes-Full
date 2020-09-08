from django.db import models
from datetime import datetime


class Contacts(models.Model):

    name = models.CharField(max_length=50, default="")
    email = models.EmailField(default='')
    contact_number = models.CharField(max_length=13, default='')
    message = models.TextField(default='')
    sent_on = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = "Messages"

