# Generated by Django 2.0.2 on 2018-02-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0017_auto_20180210_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file_id',
            field=models.BigIntegerField(default=90, max_length=200, unique=True),
        ),
    ]
