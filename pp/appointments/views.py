from datetime import datetime
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

from .serializers import AppointmentSerializer
from .models import Appointment


class GetDeleteUpdateAppointments(RetrieveUpdateAPIView):
    """ Get or update a record."""
    queryset = Appointment.objects.all().order_by('datetime')
    serializer_class = AppointmentSerializer
    lookup_field = 'pk'


class GetPostAppointments(ListCreateAPIView):
    """ List a queryset or create a new record."""
    serializer_class = AppointmentSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Appointment.objects.all().order_by('datetime')

        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date:
            start_date = datetime.strptime(start_date, '%m-%d-%Y')
        if end_date:
            end_date = datetime.strptime(end_date, '%m-%d-%Y')

        if start_date and not end_date:
            return queryset.filter(datetime__gte=start_date)
        elif start_date and end_date:
            return queryset.filter(datetime__gte=start_date, datetime__lte=end_date)
        elif end_date and not start_date:
            return queryset.filter(datetime__lte=end_date)
        else:
            return queryset
