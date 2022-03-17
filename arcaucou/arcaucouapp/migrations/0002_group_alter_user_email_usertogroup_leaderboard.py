# Generated by Django 4.0.2 on 2022-03-16 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arcaucouapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.CreateModel(
            name='UserToGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arcaucouapp.group')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arcaucouapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.DecimalField(decimal_places=0, max_digits=10)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arcaucouapp.user')),
            ],
        ),
    ]
