# Generated by Django 2.2.16 on 2021-06-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210529_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Профіль', 'verbose_name_plural': 'Профілі'},
        ),
        migrations.AlterField(
            model_name='person',
            name='player_name',
            field=models.TextField(verbose_name='ПІ'),
        ),
    ]