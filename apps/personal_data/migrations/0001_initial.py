# Generated by Django 5.1.5 on 2025-02-05 15:09

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('district', models.CharField(max_length=255, verbose_name='Район')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=255, verbose_name='Номер дома')),
                ('flat_number', models.CharField(max_length=255, verbose_name='Номер квартиры')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': '2. Адреса',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('gender', models.CharField(choices=[('None', 'Нет'), ('M', 'Мужской'), ('Ж', 'Женский')], max_length=255, verbose_name='Пол')),
                ('phone_number', models.CharField(max_length=55, validators=[django.core.validators.RegexValidator(message='Введите правильный номер телефона', regex='^(0\\d{9}|\\+996\\d{9})$')], verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': '1. Профили',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserPymentCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Номер карты должен состоять из 12 цифр', regex='^\\d{12}$')], verbose_name='Номер карты')),
                ('cardholder_name', models.CharField(max_length=255, verbose_name='Имя владельца')),
                ('expiration_date', models.DateField(verbose_name='Дата окончания срока действия')),
                ('cvv', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(message='CVV должен состоять из 3 цифр', regex='^\\d{3}$')], verbose_name='CVV')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True, verbose_name='slug')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Карта пользователя',
                'verbose_name_plural': '3. Карты ползователя',
                'ordering': ['-created_at'],
            },
        ),
    ]
