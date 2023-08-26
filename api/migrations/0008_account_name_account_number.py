# Generated by Django 4.2.4 on 2023-08-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(default='Default', max_length=128),
        ),
        migrations.AddField(
            model_name='account',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]