# Generated by Django 3.1.5 on 2021-01-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='attempt',
        ),
        migrations.AlterField(
            model_name='otp',
            name='otp',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
