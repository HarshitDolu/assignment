from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import *
from .models import *
def index(request):
    tasks=task.objects.all()
    form=taskform()
    if request.method=='POST':
        form=taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'tasks':tasks,'form':form}
    return render(request,'list/task.html',context)

def update(request,pk):
    t=task.objects.get(id=pk)
    form=taskform(instance=t)
    if request.method=='POST':
        form = taskform(request.POST,instance=t)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'list/update.html', context)


def delete_t(request,pk):
    item=task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request,'list/del.html',context)



    context={'form':form}
    return render(request,'list/update.html',context)