from django.db import models

# Create your models here.

'''
We want to know when a room was first created and evey time it gets updated
'''
class Room(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null value is allowed
    # participants = 
    updated = models.DateTimeField(auto_now=True)        # Takes a snapshot on everytime we save this item.
    created = models.DateTimeField(auto_now_add=True)    # Only takes a time stamp when we FIRST save or create this instance!

    
    def __str__(self):
        return self.name