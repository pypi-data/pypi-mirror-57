# Generated by Django 2.0 on 2018-02-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jacc', '0008_auto_20180121_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountentry',
            name='archived',
            field=models.BooleanField(default=False, verbose_name='archived'),
        ),
    ]
