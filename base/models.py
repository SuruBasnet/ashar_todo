from django.db import models

# Create your models here.
status_list = [('Done','Done'),('Not done','Not done')]

class ToDo(models.Model):
    todo_name = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=50,choices=status_list)

    def __str__(self):
        return self.name
