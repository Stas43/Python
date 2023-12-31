# Generated by Django 4.2.3 on 2023-08-27 14:52

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_4', '0020_alter_advertisement_titel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='titel',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
    ]
