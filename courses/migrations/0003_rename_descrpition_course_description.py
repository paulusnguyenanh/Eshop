# Generated by Django 3.2.6 on 2021-08-12 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210812_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='descrpition',
            new_name='description',
        ),
    ]
