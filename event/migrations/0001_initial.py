# Generated by Django 5.0.3 on 2024-03-10 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=256)),
                ('postcode', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='EventOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.organization')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='organizations',
            field=models.ManyToManyField(through='event.EventOrganization', to='event.organization'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=64, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
