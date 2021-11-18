from django.contrib import admin

# Register your models here.
from .models import Skaut, Oddil, Adresa

class SkautAdmin(admin.ModelAdmin):
    list_display = ("prezdivka", "vek", "slug")
    prepopulated_fields = { "slug" : ( "prezdivka", )}

class OddilAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "seznam_skautu")

class AdresaAdmin(admin.ModelAdmin):
    list_display = ("ulice", "oddil")

admin.site.register(Skaut, SkautAdmin)
admin.site.register(Oddil, OddilAdmin)
admin.site.register(Adresa, AdresaAdmin)

