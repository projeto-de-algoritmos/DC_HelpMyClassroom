from django.shortcuts import render
from core.api.getListStudents import getRooms
from core.api.dcMergesort import *

# Create your views here.

def home_view(request):
    students = getRooms('525987525315')
    mergeSort(students, 0, len(students)-1, 'email')
    
    print(students)
    return render(request, 'home.html',{'students':students})
