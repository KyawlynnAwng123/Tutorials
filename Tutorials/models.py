from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from .manager import UserManager
from .validators import username_validate_error

# # Create your models here.
class CustomeUser(AbstractBaseUser):
 
    name=models.CharField(max_length=50,blank=True,null=True)
    email=models.EmailField(null=True,blank=True)
 
    

    REQUIRED_FIELD = ['email']

    USERNAME_FIELD='name'

    def __str__(self):
        return self.name

# # start user models

# end user models
# start subjects models
class Subject(models.Model):
    name=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
# end subjects models

# start town model
class Town(models.Model):
    name=models.CharField(max_length=50,null=True)


    def __str__(self):
        return self.name

    
# end town model


# start person model
class Person(models.Model):
    user=models.ForeignKey(CustomeUser,on_delete=models.CASCADE,null=True)
    subject=models.ManyToManyField(Subject,related_name='subjects')
    name=models.CharField(max_length=50,validators=[username_validate_error])
    age=models.IntegerField()
    address=models.ForeignKey(Town,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='myimages',null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    persons=models.Manager()

    class Meta:
        ordering=['created']


    def __str__(self):
        return self.name


    def imageURL(self):
        try:
            url=self.image.url
        except:
            url= ''
        return url
# end person model


    @property
    def subjectsinpersons(self):
        
        return Subject.objects.filter(name='Python')



    @property

    def count_id_person(self):
        return self.id.count()


    



    

