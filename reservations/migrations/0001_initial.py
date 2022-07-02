# Generated by Django 4.0.5 on 2022-07-02 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet', models.IntegerField(default=0)),
                ('unit_payment', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TennisCourt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('Białystok', 'Białystok'), ('Gdańsk', 'Gdańsk'), ('Kraków', 'Kraków'), ('Lublin', 'Lublin'), ('Olsztyn', 'Olsztyn'), ('Poznań', 'Poznań'), ('Warszawa', 'Warszawa'), ('Wrocław', 'Wrocław')], max_length=24)),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=128)),
                ('open_hour', models.TimeField()),
                ('close_hour', models.TimeField()),
                ('hire_price', models.IntegerField()),
                ('equipment_rent', models.BooleanField()),
                ('equipment_cost', models.IntegerField(default=0)),
                ('short_description', models.CharField(default='', max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField()),
                ('reservation_start', models.TimeField()),
                ('reservation_end', models.TimeField()),
                ('reservation_cost', models.IntegerField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.profile')),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='reservations.tenniscourt')),
            ],
        ),
    ]
