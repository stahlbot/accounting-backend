# Generated by Django 4.2.4 on 2023-08-25 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_accountchart_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('non_deductible_tax', models.BooleanField(default=False)),
                ('account_chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.accountchart')),
            ],
        ),
    ]
