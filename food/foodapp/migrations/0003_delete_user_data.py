# Generated  by Django 2.2.6 on 2019-11-07 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_user_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_data',
        ),
    ]
