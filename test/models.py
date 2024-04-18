from django.db import models


class MtmFirst(models.Model):
    title = models.CharField(max_length=100)


class MtmSecond(models.Model):
    title = models.CharField(max_length=100)
    connections_to_firsts = models.ManyToManyField(MtmFirst)


class Mto(models.Model):
    title = models.CharField(max_length=100)
    mtm_first = models.ForeignKey(MtmFirst, on_delete=models.CASCADE)
