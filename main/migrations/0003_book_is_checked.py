# Generated by Django 4.0.2 on 2022-07-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_book_description_alter_book_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_checked',
            field=models.BooleanField(default='False'),
            preserve_default=False,
        ),
    ]
