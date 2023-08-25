from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo

# Create your views here.
def home(request):
    todo_objects = ToDo.objects.all() # query all objects from class todo
    content = {'todo':todo_objects} 
    return render(request,'index.html',context=content)

def create(request):
    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        ToDo.objects.create(todo_name = todo_name,description= description,status=status)
        return redirect(to='home')
    return render(request,'create.html')