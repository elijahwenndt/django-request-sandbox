# Generated by Django 4.1.3 on 2022-11-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
