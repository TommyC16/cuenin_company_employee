from django.contrib import admin

from .models import Person, Company, Employee

admin.site.register(Person)

admin.site.register(Company)

admin.site.register(Employee)

# Register your models here.
