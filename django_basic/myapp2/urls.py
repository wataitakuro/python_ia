from django.urls import path
from . import views

app_name = 'myapp2'

urlpatterns = [
    path('staff_detail/<int:pk>', views.StaffDetailView.as_view(),
         name='staff_detail')
]

