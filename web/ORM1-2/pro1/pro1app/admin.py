from django.contrib import admin

from .models import Patient,PatientAdmin
admin.site.register(Patient,PatientAdmin)
