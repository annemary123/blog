# Generated by Django 2.0.4 on 2018-04-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0003_auto_20180410_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='answer',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='register',
            name='question',
            field=models.CharField(default='', max_length=100),
        ),
    ]
