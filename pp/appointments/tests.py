from django.test import TestCase
from django.urls import reverse
import requests
import datetime
from .models import Appointment


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
        self.c = Appointment.objects.create(
            datetime="2020-11-01T03:00:00.000000Z",
            reason="SD",
            new_patient=True,
            contact_phone_number="(555)555-5555"
        )

    def tearDown(self):
        del self.a, self.b, self.c


    def test_get_appointments(self):
        response = client.get(reverse('get_post_appointments'))
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_appointment(self):
        url = reverse('get_post_appointments')
        data = {'datetime': datetime.datetime.now(),
                'new_patient': False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete_appointment(self):
          appointment = Appointment()
          response = self.client.delete(self.get_delete_update_appointments(appointment.id))
          self.assertEqual(response.status_code, HTTP_200_OK) # status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_appointment_by_pk(self):
        response = client.get(
            reverse('get_delete_update_appointments', kwargs={'pk': 10}))
        appointment = Appointment.objects.get(pk=10)
        serializer = AppointmentSerializer(appointment)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_nonexistent_appointment_by_pk(self):
        response = client.get(
            reverse('get_delete_update_appointments', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
