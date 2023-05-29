from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=200)
    completed = models.BooleanField(null=True,default=False,blank=True)

    def __str__ (self):
        return self.taskTitle
    
