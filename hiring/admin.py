from django.contrib import admin
from hiring.models import Driver


class DriverAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'company', 'truck']
    search_fields = ['first_name', 'lastname', 'truck']
    list_filter = ['company']


admin.site.register(Driver, DriverAdmin)