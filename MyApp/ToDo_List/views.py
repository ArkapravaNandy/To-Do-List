from django.shortcuts import render
from .models import list
from .forms import ListForm
from django.contrib import messages
def home(request):
    if(request.method=="POST"):
        form=ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items=list.objects.all
            messages.success(request,('Task has been successfully entered'))
            return render(request, 'home.html', {'all_items': all_items})    
            
    else:
        all_items=list.objects.all
        return render(request, 'home.html', {'all_items':all_items})

def about(request):
    name='Arkaprava Nandy'
    description='I am an Electrical Engineering undergrad at Jadavpur University, Kolkata with a knack of programming.'
    return render(request, 'about.html', {'name':name, 'desp': description})
