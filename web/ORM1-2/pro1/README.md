# Ex02 Django ORM Web Application
## Date: 14/03/2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

from django.db import models
from django.contrib import admin
# Create your models here.
# Hospital Management
# Stores patient details.
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    address = models.TextField()
    medical_history = models.TextField(blank=True, null=True)
    appointment_date = models.DateTimeField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_date = models.DateTimeField(auto_now_add=True)
    medication = models.TextField()
    dosage = models.TextField()
class PatientAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone_number','date_of_birth','gender','address','medical_history','appointment_date',
                  'diagnosis','treatment','total_amount','paid_amount','due_amount','billing_date','medication','dosage')

admin.py

from django.contrib import admin

from .models import Patient,PatientAdmin
admin.site.register(Patient,PatientAdmin)

```


## OUTPUT

![alt text](<Screenshot 2025-03-14 181816.png>)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully.
