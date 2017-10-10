from projekti.models import Stanja
from projekti.models import Openclose
from django.db import models

# Create your models here.
class Vrsta(models.Model):
    vrsta = models.CharField(max_length=50)
    def __unicode__(self):
        return self.vrsta

class Slozenost(models.Model):
    slozenost = models.CharField(max_length=50)
    def __unicode__(self):
        return self.slozenost

class Razred(models.Model):
    razred = models.CharField(max_length=50)
    def __unicode__(self):
        return self.razred

#class Stanja(models.Model):
#    stanje = models.CharField(max_length=50)
#    def __unicode__(self):
#        return self.stanje
#
#class Openclose(models.Model):
#    oc = models.CharField(max_length=50)
#    def __unicode__(self):
#        return self.oc

class Energetski_certifikat(models.Model):
    broj_certifikata = models.CharField(unique=True, max_length=200)
    zgrada = models.CharField(blank=True, max_length=200)
    narucitelj = models.CharField(blank=True, max_length=200)
    investitor = models.CharField(blank=True, max_length=200)
    opis = models.CharField(blank=True, max_length=200)
    vrsta_zgrade = models.ForeignKey(Vrsta, default=1)
    slozenost = models.ForeignKey(Slozenost, default=1)
    ovlastena_osoba = models.CharField(blank=True, max_length=50)
    gradevinski_dio = models.CharField(blank=True, max_length=50)
    strojarski_dio = models.CharField(blank=True, max_length=50)
    elektrotehnicki_dio = models.CharField(blank=True, max_length=50)
    kontakt = models.CharField(blank=True, max_length=50)
    datum_predaje = models.DateField(blank=True, null=True)
    energetski_razred = models.ForeignKey(Razred, default=1)
    ponuda = models.CharField(blank=True, max_length=100)
    racun = models.CharField(blank=True, max_length=200)
    uplata = models.CharField(blank=True, max_length=200)
    saldo = models.CharField(blank=True, max_length=20)
    stanje = models.ForeignKey(Stanja, default=1)
    biljeska = models.CharField(blank=True, max_length=200)
    energetski_certifikat = models.ForeignKey(Openclose, default=1)
    def __unicode__(self):
        return self.broj_certifikata
