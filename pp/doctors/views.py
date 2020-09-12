from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Doctor
from .serializers import DoctorSerializer


class GetPostDoctors(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
