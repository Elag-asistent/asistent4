from adresar.models import Adresar
from django.contrib import admin

class AdresarAdmin(admin.ModelAdmin):
		fieldsets = [
        ('Ime i prezime',    {'fields': ['ime','prezime']}),
        ('Poduzece',         {'fields': ['poduzece','adresa','email','web','telefon','faks','mobitel','djelatnost']}),
        ('Biljeska',         {'fields': ['biljeska']})
    ]
		list_display = ('prezime', 'ime','poduzece', 'email', 'mobitel', 'telefon', 'faks')
		list_filter = ['prezime']
		ordering = ['prezime']
		search_fields = ['ime','prezime','poduzece','email','web','telefon','faks','mobitel','adresa','djelatnost','biljeska']
		list_per_page = 75

admin.site.register(Adresar, AdresarAdmin)