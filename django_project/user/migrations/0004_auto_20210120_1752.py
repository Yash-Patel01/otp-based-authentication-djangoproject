# Generated by Django 3.1.5 on 2021-01-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210120_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.DeleteModel(
            name='OTP',
        ),
    ]