from django.shortcuts import render
from core.api.getListStudents import getRooms
from core.api.dcMergesort import *
from core.api.getTopics import getTopicos
from core.api.getMural import getMural

# Create your views here.

def home_view(request):

    filter = request.GET.get('filter')
    students = getRooms('525987525315')

    if filter == 'nome':
        mergeSort(students, 0, len(students)-1, 'nome')
    elif filter == 'id':
        mergeSort(students, 0, len(students)-1, 'id')
    elif filter == 'email':
        mergeSort(students, 0, len(students)-1, 'email')    
    else:
        print(students)
    return render(request, 'home.html',{'students':students})

def viewgetTopicos(request):
    print('topicos')
    topicos = getTopicos('525987525315')

    return render(request,'topics.html',{'topicos':topicos})

def viewgetMural(request):
    
    filtermural = request.GET.get('filtermural')
    print(filtermural)
    mural = getMural('525987525315')
    
    if filtermural == 'text':
        mergeSort(mural, 0, len(mural)-1, 'text')
    elif filtermural == 'id':
        mergeSort(mural, 0, len(mural)-1, 'id') 
    else:
        # print(mural)
        print('entrou')
    
    return render(request,'mural.html',{'mural':mural})
