# Generated by Django 2.2.16 on 2021-05-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0009_tournament_deadline_reg'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={},
        ),
        migrations.RemoveField(
            model_name='team',
            name='fuck_1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='fuck_2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='fuck_3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='fuck_4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='fuck_5',
        ),
        migrations.RemoveField(
            model_name='team',
            name='fuck_6',
        ),
        migrations.RemoveField(
            model_name='team',
            name='fuck_7',
        ),
        migrations.RemoveField(
            model_name='team',
            name='group_1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='group_2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='group_3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='group_4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='group_5',
        ),
        migrations.RemoveField(
            model_name='team',
            name='group_6',
        ),
        migrations.RemoveField(
            model_name='team',
            name='group_7',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_name_1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_name_2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_name_3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_name_4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_name_5',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_name_6',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_name_7',
        ),
        migrations.RemoveField(
            model_name='team',
            name='rate_1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='rate_2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='rate_3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='rate_4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='rate_5',
        ),
        migrations.RemoveField(
            model_name='team',
            name='rate_6',
        ),
        migrations.RemoveField(
            model_name='team',
            name='rate_7',
        ),
        migrations.RemoveField(
            model_name='team',
            name='steam_link_1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='steam_link_2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='steam_link_3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='steam_link_4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='steam_link_5',
        ),
        migrations.RemoveField(
            model_name='team',
            name='steam_link_6',
        ),
        migrations.RemoveField(
            model_name='team',
            name='steam_link_7',
        ),
        migrations.RemoveField(
            model_name='team',
            name='vuz_1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='vuz_2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='vuz_3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='vuz_4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='vuz_5',
        ),
        migrations.RemoveField(
            model_name='team',
            name='vuz_6',
        ),
        migrations.RemoveField(
            model_name='team',
            name='vuz_7',
        ),
        migrations.AddField(
            model_name='team',
            name='dop_team_list',
            field=models.TextField(default='', verbose_name='ID запасних учасників'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='team_list',
            field=models.TextField(default=' ', verbose_name='ID основних учасників'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='capitan',
            field=models.TextField(verbose_name='ID капітана'),
        ),
    ]