# Generated by Django 4.0.2 on 2022-03-01 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dehazing', '0003_rename_image_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(upload_to='profiles'),
        ),
    ]