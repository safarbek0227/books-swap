# Generated by Django 4.0.6 on 2022-07-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='user-images/', verbose_name='Image'),
        ),
    ]