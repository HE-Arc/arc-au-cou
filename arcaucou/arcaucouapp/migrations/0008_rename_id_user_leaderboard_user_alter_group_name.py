# Generated by Django 4.0.2 on 2022-03-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcaucouapp', '0007_merge_20220327_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaderboard',
            old_name='id_user',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]