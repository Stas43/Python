# Generated by Django 4.2.3 on 2023-08-07 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_lesson_4', '0003_advertisement_auction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'verbose_name': 'Объявления', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
