from asistent.energetski.models import Energetski_certifikat
from asistent.energetski.models import Vrsta
from asistent.energetski.models import Slozenost
from asistent.energetski.models import Razred
from asistent.projekti.models import Stanja
from asistent.projekti.models import Openclose
from django.contrib import admin

class EnergetskiAdmin(admin.ModelAdmin):
		fieldsets = [
        ('Broj certifikata', {'fields': ['broj_certifikata']}),
        ('Energetski certifikat', {'fields': ['zgrada','narucitelj','investitor','opis','vrsta_zgrade','slozenost','ovlastena_osoba','gradevinski_dio','strojarski_dio','elektrotehnicki_dio','kontakt','datum_predaje','energetski_razred']}),
        ('Racun', {'fields': ['ponuda','racun','uplata','saldo','stanje']}),
        ('Biljeska', {'fields': ['biljeska']}),
        ('Energetski certifikat', {'fields': ['energetski_certifikat']})
    ]
		list_display = ('broj_certifikata','zgrada','narucitelj','slozenost','energetski_razred','stanje','energetski_certifikat')
		list_filter = ['energetski_certifikat','stanje','ovlastena_osoba','energetski_razred','slozenost']
		search_fields = ['broj_certifikata','zgrada','narucitelj','biljeska','investitor','racun']

admin.site.register(Energetski_certifikat, EnergetskiAdmin)
admin.site.register(Vrsta)
admin.site.register(Slozenost)
admin.site.register(Razred)
#admin.site.register(Stanja)
#admin.site.register(Openclose)