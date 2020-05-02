from django.contrib import admin

# Register your models here.

# the module name is app_name.models
from trends.models import StockApp

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
class StockAppAdmin(admin.ModelAdmin):
    #pass
    #list_display = ('symbol','eps')
    list_display = [field.name for field in StockApp._meta.get_fields()]

admin.site.register(StockApp, StockAppAdmin)