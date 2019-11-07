# Generated by Django 2.2.6 on 2019-11-07 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webpage', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(upload_to='user')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
