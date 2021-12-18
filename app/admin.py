from django.contrib import admin
from .models import Table


class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'quantity', 'distance')
    list_filter = ('name', 'date', 'quantity', 'distance')


admin.site.register(Table, TableAdmin)
