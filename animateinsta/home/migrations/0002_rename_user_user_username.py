# Generated by Django 4.2.16 on 2024-12-25 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='username',
        ),
    ]