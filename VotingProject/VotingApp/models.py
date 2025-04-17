from django.db import models

class VoterEmail(models.Model):
    email = models.EmailField(unique=True)

class CastVote(models.Model):
    email = models.CharField(max_length=255,unique=True)
    options = models.CharField(max_length=255)
