import json
import requests
import datetime
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from pp.doctors.serializers import DoctorSerializer
from .serializers import AppointmentSerializer
from .models import Appointment
from pp.doctors.models import Doctor


client = Client()

class AppointmentTest(TestCase):

    def setUp(self):
        self.a = Appointment.objects.create(
            datetime="2020-10-31T01:00:00.000000Z",
            reason="GC",
            new_patient=False,
            contact_phone_number="(333)333-3333"
        )
        self.b = Appointment.objects.create(
            datetime="2020-11-10T02:00:00.000000Z",
            reason="NP",
            new_patient=True,
            contact_phone_number="(444)444-4444"
        )

    def tearDown(self):
        del self.a, self.b

    def test_get_appointments(self):
        response = client.get(reverse("appointments:get_post_appointments"))
        appointments = Appointment.objects.all().order_by('datetime')
        serializer = AppointmentSerializer(appointments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_appointment(self):
        url = reverse("appointments:get_post_appointments")
        data = {
            'datetime':'2020-11-01T03:00:00.000000Z',
            'reason':'SD',
            'new_patient':True,
            'contact_phone_number':'(555)555-5555',
            "doctors": [
                {"id": 1,
                    "name": "John Doe",
                    "specialization": "GE",
                    "rating": "5",
                    "booked_appointments": [12, 18],
                }
            ]
        }
        self.assertEqual(Appointment.objects.count(), 2)
        response = self.client.post(url, json.dumps(data),content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment.objects.count(), 3)
        appointment = Appointment.objects.all().last()
        self.assertEqual(getattr(appointment, 'reason'), data['reason'])

    def test_delete_appointment(self):
        url = reverse('appointments:get_delete_update_appointments', kwargs={'pk': self.b.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_appointment_by_pk(self):
        response = client.get(
            reverse('appointments:get_delete_update_appointments', kwargs={'pk': self.a.id}))
        appointment = Appointment.objects.get(pk=self.a.id)
        serializer = AppointmentSerializer(appointment)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_nonexistent_appointment_by_pk(self):
        response = client.get(
            reverse('appointments:get_delete_update_appointments', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
