# Generated by Django 2.1.5 on 2021-06-29 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_profile_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='desc',
            new_name='bio',
        ),
    ]
