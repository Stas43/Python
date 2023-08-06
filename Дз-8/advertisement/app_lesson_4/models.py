from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisement(models.Model):
    titel = models.CharField("Заголовок", max_length=50)
    description = models.TextField("Описание")
    author = models.CharField("Автор", max_length=27)
    auction = models.BooleanField("торг", help_text="Отметьте, если торг уместен")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'


    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html (
                '<span style = "color: green; font-weight: bold;"> Сегодня в {} </span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color: red; font-weight: bold;"> Сегодня в {} </span>', updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')
