from django.db import models

# set up Job class to be ready for database
class Job(models.Model) :
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length = 200)
