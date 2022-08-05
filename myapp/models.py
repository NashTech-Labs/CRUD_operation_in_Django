from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.IntegerField()
    
    # def __str__(self):
    #     return self.firstname 

class parents(models.Model):
    # company=models.ForeignKey(employees, on_delete=models.CASCADE)
    mothername=models.CharField(max_length=10)
    fathername=models.CharField(max_length=10)

class empadd(models.Model):
    city=models.CharField(max_length=10)
    state=models.CharField(max_length=10)
    country=models.CharField(max_length=10)

class hobbies(models.Model):
    Likes=models.CharField(max_length=10)
    Dislikes=models.CharField(max_length=10)



