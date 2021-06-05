# Generated by Django 2.2.16 on 2021-06-05 16:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0012_auto_20210529_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='imagin2',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='imagin3',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='tournament_text',
        ),
        migrations.AddField(
            model_name='tournament',
            name='content',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Контент'),
            preserve_default=False,
        ),
    ]