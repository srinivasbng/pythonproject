from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    #lastname = models.CharField(max_length=100)
    dob=models.DateField(null=True, blank=True)
    eid=models.IntegerField()
    email=models.EmailField(max_length=100)
    data=models.TextField(max_length=400)


    def __str(self):
        return self.name

class Studentlogin(models.Model):
    name=models.CharField(max_length=100)
    eid=models.IntegerField()

    def __str(self):
        return self.name