from django.db import models

class Sii_Api(models.Model):
    # Id sera automatique
    idApp = models.IntegerField(blank=False)
    date = models.DateTimeField()
    type = models.CharField(max_length=70, blank=False, default='')
    valeur = models.TextField(blank=False, default='')
    alerte = models.IntegerField(default=0)
    messageAlerte = models.CharField(max_length=255,blank=True, default='')

class User(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
