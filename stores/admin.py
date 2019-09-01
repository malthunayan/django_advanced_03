from django.contrib import admin
from .models import Store


class StoreAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'description', 'added')
	search_fields = ['name', 'description']
	list_filter = ['added']
	list_display_links = ['name']
	list_editable = ['description']


# Register your models here.
admin.site.register(Store, StoreAdmin)