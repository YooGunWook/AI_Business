from django.db import models

# Create your models here.
class Predict(models.Model):
    group1 = models.IntegerField()
    group2 = models.IntegerField()
    group3 = models.IntegerField()
    weekend = models.IntegerField()
    soccer = models.FloatField()
    small_dust = models.FloatField()
    rainfall = models.FloatField()
    meantemp = models.FloatField()
    constant = models.IntegerField(default=1)