# Generated by Django 3.1.1 on 2020-09-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointment_doctor_list'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='booked_appointments',
            field=models.ManyToManyField(blank=True, related_name='doctors', to='appointments.Appointment'),
        ),
    ]
