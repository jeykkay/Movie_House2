from django.contrib import admin
from django.utils.safestring import mark_safe

from movie.models import Movie, Genre, Director, Actor, Hall, Seat, Session, Booking


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="40" height="50"')

    get_image.short_description = "Фото"


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'first_name', 'last_name', 'age']
    list_display_links = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'movie__title']

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="40" height="50"')

    get_image.short_description = 'Фото'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_image', 'release_date']
    list_filter = ['title', 'release_date', 'genres']
    search_fields = ['title', 'actors__first_name', 'actors__last_name']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="30" height="40')

    get_image.short_description = 'Постер'


admin.site.register(Hall)
admin.site.register(Seat)
admin.site.register(Session)
admin.site.register(Booking)
