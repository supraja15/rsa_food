# Generated  by Django 2.2.6 on 2019-11-07 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0003_delete_user_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='southindianfood',
            name='id',
        ),
        migrations.AlterField(
            model_name='southindianfood',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
