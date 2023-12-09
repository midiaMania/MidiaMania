# Generated by Django 4.2.7 on 2023-12-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('synopsis', models.TextField()),
                ('directors', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('running_time', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('img', models.ImageField(upload_to='frontend/static/images/games/')),
                ('copias', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('categories', models.ManyToManyField(to='movies.category')),
            ],
        ),
    ]