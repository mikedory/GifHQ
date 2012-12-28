from gifserver.models import Gifsite, Gif
from django.contrib import admin


# add some custom field handling for sites in the admin panel
class GifsiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'url', 'active']}),
        ('Date information', {'fields': ['date_added'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'url', 'date_added', 'active')
    list_filter = ('name',)


# add some extra fields for gifs too
class GifAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'url', 'active']}),
        ('Date information', {'fields': ['date_added'], 'classes': ['collapse']}),
    ]
    list_display = ('gifsite', 'name', 'url', 'date_added', 'active')
    list_filter = ('name',)

# slap those new fields in there
admin.site.register(Gifsite, GifsiteAdmin)
admin.site.register(Gif, GifAdmin)
