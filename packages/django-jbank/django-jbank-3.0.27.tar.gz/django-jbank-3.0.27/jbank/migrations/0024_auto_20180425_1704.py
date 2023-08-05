# Generated by Django 2.0.4 on 2018-04-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbank', '0023_auto_20180419_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='payout',
            name='full_path',
            field=models.TextField(blank=True, editable=False, verbose_name='full path'),
        ),
        migrations.AlterField(
            model_name='payout',
            name='state',
            field=models.CharField(blank=True, choices=[('W', 'waiting processing'), ('U', 'waiting upload'), ('D', 'uploaded'), ('P', 'paid'), ('C', 'canceled'), ('E', 'error')], db_index=True, default='W', max_length=1, verbose_name='state'),
        ),
    ]
