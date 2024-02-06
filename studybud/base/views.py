from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'Design with me'},
#     {'id':3, 'name':'Frontend developers'}
# ]

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
    context = {}
    return render(request, 'base/room_form.html', context)