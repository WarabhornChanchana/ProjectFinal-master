# Generated by Django 4.2.9 on 2024-02-05 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='account',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]