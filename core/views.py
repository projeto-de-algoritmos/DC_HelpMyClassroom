from django.shortcuts import render
from core.api.getListStudents import getRooms
from core.api.dcMergesort import *
from core.api.getTopics import getTopicos
from core.api.getMural import getMural

# Create your views here.

def home_view(request):
    print('entrou')
    students = getRooms('525987525315')
    # mergeSort(students, 0, len(students)-1, 'email')
    
    print(students)
    return render(request, 'home.html',{'students':students})

def viewgetTopicos(request):
    print('topicos')
    topicos = getTopicos('525987525315')

    return render(request,'topics.html',{'topicos':topicos})

def viewgetMural(request):
    print('mural')
    mural = getMural('525987525315')

    return render(request,'mural.html',{'mural':mural})        
