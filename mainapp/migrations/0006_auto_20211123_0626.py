# Generated by Django 3.2.8 on 2021-11-23 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20211123_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintsdetails',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='complaintsdetails',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
