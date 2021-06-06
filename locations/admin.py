from django.contrib import admin

from .models import Business, Neighborhood, Contact, Admin

admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Contact)
admin.site.register(Admin)