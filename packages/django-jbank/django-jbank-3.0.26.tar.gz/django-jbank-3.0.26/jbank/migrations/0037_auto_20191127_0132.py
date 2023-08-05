# Generated by Django 2.2.3 on 2019-11-27 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jbank', '0036_wsediconnection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wsediconnection',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='wsediconnection',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='jbank.PayoutParty', verbose_name='customer'),
            preserve_default=False,
        ),
    ]
