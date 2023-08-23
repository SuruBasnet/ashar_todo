from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo

# Create your views here.
def home(request):
    todo_objects = ToDo.objects.all() # query all objects from class todo
    content = {'todo':todo_objects} 
    return render(request,'index.html',context=content)

def about(request):
    return HttpResponse('We do programming!')