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
    rooms = Room.objects.all() # objects is the model Manager! A python way to communicate with the models / DB
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

'''
Working with path parameters
'''
def room(request, pk):
    room = Room.objects.get(id=pk)   # Retrieves a single instance from the Room DB with the given id
    context = {'room':room}
    return render(request, 'base/room.html', context)