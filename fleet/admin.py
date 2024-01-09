from django.contrib import admin
from fleet.models import Truck, TruckMake, TruckModel



class TruckMakeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']



class TruckModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class TruckAdmin(admin.ModelAdmin):
    list_display = ['unit_number', 'driver', 'year', 'make', 'model']
    search_fields = ['unit_number', 'driver']
    list_filter = ['make', 'model', 'year', 'carrier']


admin.site.register(Truck, TruckAdmin)
admin.site.register(TruckMake, TruckMakeAdmin)
admin.site.register(TruckModel, TruckModelAdmin)

