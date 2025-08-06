from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('To-Do','To-Do'),
        ('In Progress','In Progress'),
        ('Done','Done'),
    ]
    PRIORITY_CHOICES = [
        ('High Priority','High Priority'),
        ('Low Priority','Low Priority'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Low Priority')
    dueDate = models.DateField()
