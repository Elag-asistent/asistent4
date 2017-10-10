from projekti.models import Projekt
from projekti.models import Stanja
from projekti.models import Faze
from projekti.models import Openclose
from django.contrib import admin

class ProjektAdmin(admin.ModelAdmin):
		fieldsets = [
        ('T.D.', {'fields': ['td']}),
        ('Projekt', {'fields': ['gradevina','narucitelj','investitor','faza','opis','projektant','suradnik','kontakt','datum_predaje']}),
        ('Racun', {'fields': ['ponuda','racun','uplata','saldo','stanje']}),
        ('Biljeska', {'fields': ['biljeska']}),
        ('Projekt', {'fields': ['projekt']})
    ]
		list_display = ('td', 'gradevina', 'narucitelj', 'investitor','faza','racun','stanje','projekt')
		list_filter = ['projekt','stanje','projektant','suradnik','faza']
		search_fields = ['td','gradevina','narucitelj','biljeska', 'investitor', 'racun']

admin.site.register(Projekt, ProjektAdmin)
admin.site.register(Stanja)
admin.site.register(Faze)
admin.site.register(Openclose)