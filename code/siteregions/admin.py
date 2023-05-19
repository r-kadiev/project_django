from django.contrib import admin
from .models import Site, Region, SiteRegion


class SiteAdmin(admin.ModelAdmin):
    list_display = ['domain']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']


class SiteRegionAdmin(admin.ModelAdmin):
    list_display = ['region_id', 'site_id', 'type', 'key', 'value']


admin.site.register(Site, SiteAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(SiteRegion, SiteRegionAdmin)
