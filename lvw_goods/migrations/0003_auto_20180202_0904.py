# Generated by Django 2.0.1 on 2018-02-02 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lvw_goods', '0002_typeinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodinfo',
            name='gadv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goodinfo',
            name='gtype',
            field=models.IntegerField(default=0),
        ),
    ]
