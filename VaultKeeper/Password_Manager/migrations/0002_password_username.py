# Generated by Django 4.1 on 2023-04-05 06:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Password_Manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
