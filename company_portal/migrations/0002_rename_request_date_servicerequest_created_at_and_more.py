# Generated by Django 5.1.2 on 2024-10-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='request_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='servicerequest',
            old_name='description',
            new_name='request_details',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='service_name',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='status',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='service_category',
            field=models.CharField(default='Gas Delivery and Distribution', max_length=100),
        ),
    ]
