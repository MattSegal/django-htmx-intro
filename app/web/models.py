from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.email}"
