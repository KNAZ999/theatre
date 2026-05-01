from django.contrib import admin
from .models import Play, Actor, Show, Booking


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday')


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('play_name', 'starts_at')
    filter_horizontal = ('actors',)
    search_fields = ('play__title',)

    @admin.display(description='Спектакль')
    def play_name(self, obj):
        return obj.play.title


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['show', 'seats', 'owner', 'created_at']
    list_filter = ['show', 'owner']
    search_fields = ['owner__username', 'show__play__title']