# Generated by Django 3.2 on 2023-01-06 05:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import reviews.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите категорию', max_length=256, unique=True, verbose_name='Категория')),
                ('slug', models.SlugField(help_text='Укажите адрес', unique=True, verbose_name='Адрес')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите жанр', max_length=256, unique=True, verbose_name='Жанр')),
                ('slug', models.SlugField(help_text='Укажите адрес', unique=True, verbose_name='Адрес')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название произведения', max_length=256, unique=True, verbose_name='Название произведение')),
                ('year', models.PositiveIntegerField(db_index=True, help_text='Введите год выпуска', validators=[reviews.validators.validate_year], verbose_name='Год выпуска произведения')),
                ('description', models.TextField(blank=True, help_text='Введите текст описания', null=True, verbose_name='Описание произведения')),
                ('category', models.ForeignKey(help_text='Укажите категорию', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.category', verbose_name='Категория произведения')),
                ('genre', models.ManyToManyField(help_text='Укажите жaнры', related_name='titles', through='reviews.GenreTitle', to='reviews.Genre', verbose_name='Жанры произведения')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
