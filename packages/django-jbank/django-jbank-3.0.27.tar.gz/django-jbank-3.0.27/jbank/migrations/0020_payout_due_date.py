# Generated by Django 2.0 on 2018-02-09 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbank', '0019_auto_20180209_0437'),
    ]

    operations = [
        migrations.AddField(
            model_name='payout',
            name='due_date',
            field=models.DateField(blank=True, db_index=True, default=None, null=True, verbose_name='due date'),
        ),
    ]
