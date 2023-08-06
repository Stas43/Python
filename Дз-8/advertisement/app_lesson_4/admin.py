from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'titel', 'description', 'price', 'auction', 'created_date', 'updated_date']
    list_filter = ['auction', 'created_at']

    actions = ['make_action_as_false','make_action_as_true']

    @admin.action(description = 'Убрать возможность торга')
    def make_action_as_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset):
        queryset.update(auction=True)

    fieldsets = (
        ('Общие', {
            'fields': ('titel','description')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })

    )

admin.site.register(Advertisement, AdvertisementAdmin)




