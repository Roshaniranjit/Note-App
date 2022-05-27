from django.db import models

# Create your models here.
 #title
 #date
 #description

 #crude operation

class Note(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.date}and{self.title}'
