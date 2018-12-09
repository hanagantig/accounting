# Generated by Django 2.1.4 on 2018-12-09 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='company.Company', verbose_name='Компания'),
        ),
    ]