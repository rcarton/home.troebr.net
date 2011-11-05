from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.forms.fields import CharField
import datetime
import inspect
import sys


class Place(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return "%s" % (self.name,)

# User
class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


# Modules
class Module(models.Model):
    
    # List of module types
    module_types= None
    
    class Meta:
        abstract = True
    
    place = models.OneToOneField(Place)
    name = models.CharField(max_length=100)
    
    @classmethod
    def get_module_types(cls):
        if not cls.module_types:
            clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
            cls.module_types = [m for m in clsmembers if issubclass(m[1], cls) and m[1] != cls]
        return cls.module_types
    
    def __unicode__(self):
        return "%s" % (self.name,)
    
class Countdown(Module):
    
    MODULE_NAME = 'countdown'

    end_date = models.DateTimeField()

    def __unicode__(self):
        return "%s - %s" % (self.name, self.end_date)
    
    def get_delta(self):
        return self.end_date - datetime.datetime.now()
    
    def get_dict(self):
        return { 
                'end_date': self.end_date,
                'delta': self.get_delta()
               }  
     
class MessageList(Module):
    MODULE_NAME = 'messagelist'
    
    
class Item(models.Model):
    date = models.DateTimeField(auto_now=True)
    poster = models.ForeignKey(User)
    
class Message(Item):
    messagelist = models.ForeignKey(MessageList)
    value = models.CharField(max_length=500)
    
    def __unicode__(self):
        return "%s@%s: %s[..]" % (self.poster, self.date, self.value[0:20])
    
    