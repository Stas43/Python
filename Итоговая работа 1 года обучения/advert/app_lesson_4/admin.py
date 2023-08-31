from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'titel', 'description', 'price', 'auction', 'created_date', 'updated_date', 'photo']
    list_filter = ['auction', 'created_at']

    actions = ['make_action_as_false','make_action_as_true']

    @admin.action(description = 'Убрать возможность торга')
    def make_action_as_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.display(description='Thumbnail')
    def get_thumbnail(self, obj):
        return format_html('<img src="{}" width="50px" height="50px" />', obj.photo.url)
    get_thumbnail.short_description = 'Thumbnail'

    fieldsets = (
        ('Общие', {
            'fields': ('titel','description', 'user', 'photo')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
        })
    )



admin.site.register(Advertisement, AdvertisementAdmin)