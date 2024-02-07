from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# Create your views here.

# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'Design with me'},
#     {'id':3, 'name':'Frontend developers'}
# ]

'''
Retrieve the room instances from the Room Model / DB and display them in the home page
'''
def home(request):
    rooms = Room.objects.all() # objects is the model Manager! A python way to communicate with the models / DB - query the DB for all objects
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

'''
Working with path parameters
'''
def room(request, pk):
    room = Room.objects.get(id=pk)   # Retrieves a single instance from the Room DB with the given id - query the DB for a single object
    context = {'room':room}
    return render(request, 'base/room.html', context)

'''
Now we want to add the CRUD operations!
The core of any functionality on a website!
We want to learn how to work with a database outside the django Admin Panel!
'''

def createRoom(request):
    form = RoomForm()                  # If its a GET request just display the form empty to fill up
    
    if request.method == "POST":
        # print(request.POST)          # Prints: <QueryDict: {'csrfmiddlewaretoken': ['5IhuCmLnA2ABPdUTz0vpGZUMGLgXxLHXswJz6qaPk2IswFv8B4Bvcp680tbcLkXR'], 'host': ['1'], 'topic': ['2'], 'name': ['Lets LEARN!'], 'description': ['']}>
        form = RoomForm(request.POST)  # populating the form with the data that was submitted
        if form.is_valid():
            form.save()
            return redirect('home')    # If the form is good then redirect the user to the home page ('home' being the name attribute of the url pattern)
        
    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method=="POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'base/room_form.html', context)