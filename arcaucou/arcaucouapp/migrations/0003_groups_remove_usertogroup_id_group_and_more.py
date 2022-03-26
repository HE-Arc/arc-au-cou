# Generated by Django 4.0.2 on 2022-03-24 13:44

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('arcaucouapp', '0002_group_alter_user_email_usertogroup_leaderboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('password', models.CharField(max_length=255)),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='usertogroup',
            name='id_group',
        ),
        migrations.RemoveField(
            model_name='usertogroup',
            name='id_user',
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserToGroup',
        ),
    ]
