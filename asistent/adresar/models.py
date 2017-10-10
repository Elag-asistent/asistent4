from django.db import models

# Create your models here.
class Adresar(models.Model):
    ime = models.CharField(blank=True, max_length=200)
    prezime = models.CharField(max_length=200)
    prezime.alphabetic_filter = True
    poduzece = models.CharField(blank=True, max_length=200)
    adresa = models.CharField(blank=True, max_length=300)
    email = models.CharField(blank=True, max_length=200)
    web = models.CharField(blank=True, max_length=200)
    telefon = models.CharField(blank=True, max_length=200)
    faks = models.CharField(blank=True, max_length=200)
    mobitel = models.CharField(blank=True, max_length=200)
    djelatnost = models.CharField(blank=True, max_length=200)
    biljeska = models.TextField(blank=True, max_length=200)
    def __unicode__(self):
        return self.prezime