from django.db import models
from django.contrib.auth.models import AbstractUser

class Education(models.Model):
    name = models.CharField(max_length=20,default = False,null = True,blank = True)
    def __str__(self):
        return str(self.id)
        

class Sports(models.Model):
    name = models.CharField(max_length=20,default = True,null = True,blank = True)
    def __str__(self):
        return str(self.id)
        
class MyUser(AbstractUser):
    phone_number = models.CharField(max_length=20,default = True,null = True,blank = True)
    address = models.CharField(max_length = 21,default = True,blank = True,null = True)
    education = models.ForeignKey('Education',on_delete=models.CASCADE,default = None,blank = True,null = True)
    sports = models.ManyToManyField('Sports',default = None,blank = True,null = True)
    # education = models.ForeignKey('Education',on_delete=models.CASCADE,default = True,blank = True,null = True,related_name='education')
    # sports = models.ManyToManyField('Sports',default = True,blank = True,null = True,related_name='sports')

    def __str__(self):
        return str(self.id)

