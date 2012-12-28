from gifserver.models import Gifsite, Gif
from django.contrib import admin


# adding some custom field handling for the admin panel
class GifsiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'url']}),
        ('Date information', {'fields': ['date_added'], 'classes': ['collapse']}),
    ]

admin.site.register(Gifsite, GifsiteAdmin)
admin.site.register(Gif)
