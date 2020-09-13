from rest_framework.serializers import ModelSerializer
from .models import Doctor


class DoctorSerializer(ModelSerializer):

    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "specialization",
            "rating",
            "booked_appointments"
        ]
        extra_kwargs = {'booked_appointments': {'required': False ,'read_only': True}}
