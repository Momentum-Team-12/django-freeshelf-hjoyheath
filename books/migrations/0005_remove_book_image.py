# Generated by Django 4.0.4 on 2022-05-10 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]