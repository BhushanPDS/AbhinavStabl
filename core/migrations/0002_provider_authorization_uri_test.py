# Generated by Django 3.2.12 on 2023-02-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='authorization_uri_test',
            field=models.TextField(blank=True, null=True),
        ),
    ]