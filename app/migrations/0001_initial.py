# Generated by Django 3.0.6 on 2020-05-30 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChosenCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.IntegerField(choices=[(1, '%H:%M:%S'), (2, '%l:%M:%p'), (3, '%r'), (4, '%R'), (5, '%T')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('timezone', timezone_field.fields.TimeZoneField(default='Europe/Lisbon')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.ManyToManyField(through='app.ChosenCountry', to='app.Country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chosencountry',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Country'),
        ),
        migrations.AddField(
            model_name='chosencountry',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
