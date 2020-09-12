from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('api/v1/doctors/',
        views.GetPostDoctors.as_view(),
        name="get_post_doctors"
    ),
]
