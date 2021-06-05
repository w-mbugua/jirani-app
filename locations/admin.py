from django.contrib import admin

from .models import Business, Neighborhood

admin.site.register(Neighborhood)
admin.site.register(Business)
