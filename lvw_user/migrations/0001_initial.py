# Generated by Django 2.0.1 on 2018-01-20 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemil', models.EmailField(max_length=30)),
                ('urelname', models.CharField(default='', max_length=20)),
                ('uadr', models.CharField(default='', max_length=100)),
                ('uphone', models.CharField(default='', max_length=11)),
            ],
        ),
    ]
