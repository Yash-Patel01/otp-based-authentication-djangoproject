# Generated by Django 3.1.5 on 2021-01-20 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_loginattempts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginattempts',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
