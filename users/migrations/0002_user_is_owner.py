# Generated by Django 4.0.3 on 2022-04-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
