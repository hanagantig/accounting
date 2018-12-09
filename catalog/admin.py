from django.contrib import admin
from catalog.models import Service

admin.site.register(Service, admin.ModelAdmin)