from django.contrib import admin

from maintenance.models import Status, Case, Note, Odometer


admin.site.register(Status)
admin.site.register(Case)
admin.site.register(Note)
admin.site.register(Odometer)
