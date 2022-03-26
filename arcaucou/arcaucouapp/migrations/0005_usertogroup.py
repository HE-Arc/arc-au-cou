# Generated by Django 4.0.2 on 2022-03-26 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arcaucouapp', '0004_group_delete_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arcaucouapp.group')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
