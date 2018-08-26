from django.shortcuts import render
from .models import Services
# Create your views here.

def portfolio(request):
    services = Services.objects.all()
    return render(request, "service/service.html", {'services':services})
