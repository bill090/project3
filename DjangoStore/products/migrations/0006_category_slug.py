# Generated by Django 3.1.8 on 2021-04-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210426_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=300),
        ),
    ]