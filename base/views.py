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
    content = {'method':'create'}
    return render(request,'create.html',context=content)

def edit(request,pk):
    todo_object = ToDo.objects.get(id=pk)
    if request.method == 'POST':
        new_todo_name = request.POST.get('name')
        new_description = request.POST.get('description')
        new_status = request.POST.get('status')
        todo_object.todo_name = new_todo_name
        todo_object.description = new_description
        todo_object.status = new_status
        todo_object.save()
        return redirect(to='home')
    content = {'method':'edit','object':todo_object}
    return render(request,'create.html',context=content)