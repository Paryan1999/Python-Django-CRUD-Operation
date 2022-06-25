from django.db import models


class Position(models.Model):
    title=models.CharField(max_length=30)

    def __str__(self):
        return self.title
    




# Create your models here.
class Employee(models.Model):
    full_name=models.CharField(max_length=25)
    mobile=models.CharField(max_length=10)
    employee_id=models.CharField(max_length=20)
    email_id=models.EmailField(default="")
    position=models.ForeignKey(Position ,on_delete=models.CASCADE,null=True)
    
