from django.db import models
from django.contrib.auth.models import User

# Create your models here.

""" 
    Category 
        - name
"""
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name 

""" 
    Task 
        - Title 
        - Description 
        - category
        - start_datetime 
        - end_datetime  
        - completed 
        - user 
"""

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"
    