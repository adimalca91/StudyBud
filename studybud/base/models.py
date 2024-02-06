from django.db import models
from django.contrib.auth.models import User

# Create your models here.

''' One Topic can have a lot of rooms, whereas a room can have only one Topic'''
class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

'''
We want to know when a room was first created and evey time it gets updated
'''
class Room(models.Model):
    host =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # One host/User can have lots of Rooms whereas a room can have only one host
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null value is allowed
    # participants = 
    updated = models.DateTimeField(auto_now=True)        # Takes a snapshot on everytime we save this item.
    created = models.DateTimeField(auto_now_add=True)    # Only takes a time stamp when we FIRST save or create this instance!

    
    def __str__(self):
        return self.name
    

''' Each Room is going to have a message - One Room can have many messages / posts '''
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # A User can have many messages whereas a message can only have one User (message=post)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # Establish one-to-many relationship between Message and Room
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)       
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]