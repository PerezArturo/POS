from django.db import models
from django.contrib.auth.models import User
from POS import settings


class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True
