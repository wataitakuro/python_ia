from django.shortcuts import render

# Create your views here.

class StaffDetailView(generic.DetailView):
    model = Staff
    template_name = 'myapp2/staff_detail.html'