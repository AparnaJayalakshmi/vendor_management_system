# Generated by Django 5.0.6 on 2024-07-11 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='acknowledgement_date',
            new_name='acknowledgment_date',
        ),
    ]