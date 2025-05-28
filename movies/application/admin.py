from django.contrib import admin
from .models import tollywood # No space before `.models` is fine too

class tollywoodAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'director', 'images', 'date_of_release', 'actress', 'rating', 'collections')
    list_filter = ('date_of_release',)
    search_fields = ('movie_name', 'director', 'producer')

admin.site.register(tollywood, tollywoodAdmin)
