# Generated by Django 2.0.2 on 2018-02-11 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0029_auto_20180211_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JU', 'Junior'), ('SE', 'Senior')], default='FR', max_length=2),
        ),
        migrations.AlterField(
            model_name='files',
            name='file_id',
            field=models.CharField(blank=True, default='9511428216477609084', max_length=200),
        ),
    ]
