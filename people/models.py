from django.db import models

class People(models.Model):
    '''
    
    '''
    name = models.CharField(max_length=25, help_text='Enter you name', default='Raghav')
    phone = models.CharField(max_length=10, help_text='Enter you mobile number')
    email = models.EmailField()
    image = models.ImageField(upload_to='static/img/')
    moto = models.TextField()

    def __str__(self):
        return f'{self.id} {self.name} {self.phone}'
    

