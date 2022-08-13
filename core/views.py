from django.shortcuts import render
from core.api.getListStudents import getRooms
from core.api.dc import *

# Create your views here.

def home_view(request):
    students = getRooms('525987525315')
    
    print(students)
    return render(request, 'home.html',{'students':students})
