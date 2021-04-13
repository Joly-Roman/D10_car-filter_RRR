from django.contrib import admin
from cars.models import *

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass