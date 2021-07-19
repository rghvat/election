from django.db import models

from people.models import People

# Create your models here.
class Poll(models.Model):
    '''
    
    '''
    name = models.CharField(max_length=125)
    people = models.ManyToManyField(People, related_name='candidate')
