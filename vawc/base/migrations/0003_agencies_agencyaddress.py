# Generated by Django 4.2.4 on 2023-11-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_agencies_contactnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencies',
            name='agencyAddress',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]