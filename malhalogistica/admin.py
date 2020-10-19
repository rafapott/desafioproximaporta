from django.contrib import admin

# Register your models here.

from .models import Mapa, Distancia

admin.site.register(Mapa)
admin.site.register(Distancia)