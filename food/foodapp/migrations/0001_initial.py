# Generated  by Django 2.2.6 on 2019-11-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChineseFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NorthIndiaFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SouthIndianFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
