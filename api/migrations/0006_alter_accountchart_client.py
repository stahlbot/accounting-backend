# Generated by Django 4.2.4 on 2023-08-25 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_accountchart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountchart',
            name='client',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.client'),
        ),
    ]