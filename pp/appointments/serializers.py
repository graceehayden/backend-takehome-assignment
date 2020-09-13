from rest_framework.serializers import ModelSerializer
from .models import Appointment
from pp.doctors.serializers import DoctorSerializer


class AppointmentSerializer(ModelSerializer):
    doctors = DoctorSerializer(many=True)

    class Meta:
        model = Appointment
        fields = [
            "id",
            "datetime",
            "reason",
            "new_patient",
            "contact_phone_number",
            "doctors",
        ]
        extra_kwargs = {'doctors': {'required': False}}

    def create(self, validated_data):
        doctor_validated_data = validated_data.pop('doctors')
        appointment = Appointment.objects.create(**validated_data)
        doctors_serializer = self.fields['doctors']
        appts = []
        for each in doctor_validated_data:
            if 'booked_appointments' in each.keys():
                if each['booked_appointments'].contains(appointment.id):
                    raise serializers.ValidationError("This appointment time is booked!")
            else:
                each['booked_appointments'] = str(appointment.id)
                # should be appending to list
        doctor_list = doctors_serializer.create(doctor_validated_data)
        return appointment
