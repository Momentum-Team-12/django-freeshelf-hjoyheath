# Generated by Django 4.0.4 on 2022-05-09 23:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='img/'),
            preserve_default=False,
        ),
    ]
