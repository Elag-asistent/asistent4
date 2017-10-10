from nadzori.models import Nadzor
from projekti.models import Stanja
from projekti.models import Openclose
from django.contrib import admin

class NadzorAdmin(admin.ModelAdmin):
		fieldsets = [
        ('Imenovanje', {'fields': ['imenovanje']}),
        ('Nadzor', {'fields': ['gradevina','narucitelj','investitor','opis','nadzorni_inzenjer','kontakt','zavrsno_izvjesce','datum_tehnickog_pregleda']}),
        ('Racun', {'fields': ['ponuda','racun','uplata','saldo','stanje']}),
        ('Biljeska', {'fields': ['biljeska']}),
        ('Projekt', {'fields': ['nadzor']})
    ]
		list_display = ('imenovanje', 'gradevina', 'narucitelj', 'investitor','zavrsno_izvjesce','stanje','nadzor')
		list_filter = ['nadzor','stanje','nadzorni_inzenjer']
		search_fields = ['imenovanje','gradevina','narucitelj','biljeska','investitor','racun']

admin.site.register(Nadzor, NadzorAdmin)
#admin.site.register(Stanja)
#admin.site.register(Openclose)