# Generated by Django 2.0.1 on 2018-02-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lvw_goods', '0004_auto_20180202_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeinfo',
            name='pid',
            field=models.IntegerField(default=0),
        ),
    ]