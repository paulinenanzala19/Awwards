# Generated by Django 4.0.5 on 2022-06-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theawwards', '0003_post_image_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
