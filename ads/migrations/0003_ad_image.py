# Generated by Django 2.0 on 2018-02-10 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ad_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]