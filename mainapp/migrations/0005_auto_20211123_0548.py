# Generated by Django 3.2.8 on 2021-11-23 05:48

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20211123_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaintsdetails',
            name='image',
        ),
        migrations.AddField(
            model_name='complaintsdetails',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=mainapp.models.upload_image_path),
        ),
    ]
