# Generated by Django 2.0.2 on 2018-04-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0049_auto_20180329_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
