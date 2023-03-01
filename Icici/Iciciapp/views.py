from django.shortcuts import render
from django.shortcuts import render
from .models import Employee_Details
from rest_framework.views import APIView
from rest_framework.viewsets import views
# Create your views here.
def show(r):
    results=Employee_Details.objects.all()
    print(results)
    return render(r,'display.html',{'data':results})
