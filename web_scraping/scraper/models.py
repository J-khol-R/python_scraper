from django.db import models

class Hockey(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    ot_losses = models.IntegerField(null=True)
    win_percentage = models.FloatField(null=True)
    goals_for = models.IntegerField(null=True)
    goals_against = models.IntegerField(null=True)
    plus_minus = models.IntegerField(null=True)
