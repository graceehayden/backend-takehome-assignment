from rest_framework.serializers import ModelSerializer
from .models import Appointment

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            "id",
            "datetime",
            "reason",
            "new_patient",
            "contact_phone_number",
        ]



"""
Data:
    {
        "id": 9,
        "datetime": "2020-09-12T01:15:35.856712Z",
        "reason": "GC",
        "new_patient": false,
        "contact_phone_number": ""
    },
    {
        "id": 10,
        "datetime": "2020-09-12T01:16:21.449400Z",
        "reason": "Annual Checkup",
        "new_patient": true,
        "contact_phone_number": ""
    }
    {'id': 11, 'datetime': '2020-09-12T01:20:41.642329Z', 'reason': 'GC', 'new_patient': False, 'contact_phone_number': ''}
"""
