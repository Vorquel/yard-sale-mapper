from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 60)
    address = models.CharField(max_length = 200)
    radius = models.FloatField(default = 5)

class Yardsale(models.Model):
    where = models.CharField(max_length = 200)
    s_time = models.TimeField()
    e_time = models.TimeField()
    date = models.DateField()
    posted = models.DateTimeField()

class Distance(models.Model):
    sale1 = models.ForeignKey('Yardsale')
    sale2 = models.ForeignKey('Yardsale', related_name = '+')
    dist = models.FloatField()

