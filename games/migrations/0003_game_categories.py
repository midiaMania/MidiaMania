# Generated by Django 4.2.7 on 2023-12-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(to='games.category'),
        ),
    ]