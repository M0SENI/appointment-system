# Generated by Django 4.2.11 on 2025-02-05 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_rename_email_acceptedappointment_appointment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
