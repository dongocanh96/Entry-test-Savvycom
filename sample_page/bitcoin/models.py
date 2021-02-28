from django.db import models

class Info(models.Model):
    price = models.CharField(max_length=200)
    marketCap = models.CharField(max_length=200)

    def __str__(self):
        return self
