from django.contrib import admin
from processmap.models import MapAreaLink


class MapAreaLinkAdmin (admin.ModelAdmin):
	list_display = ['map_area', 'page']


admin.site.register(MapAreaLink, MapAreaLinkAdmin)
