from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    description = models.TextField()
    tags = models.CharField(max_length=1024)
    
    topic = models.CharField(max_length=256)
    language = models.CharField(max_length=32)
    duration = models.IntegerField()  # in hours
    difficulty = models.DecimalField(max_digits=2, decimal_places=1)
    detail = models.DecimalField(max_digits=2, decimal_places=1)
    userscore = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name
    
    def get_tags(self):
        return self.tags.split(',')


class Trajectory(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    description = models.TextField()
    tags = models.CharField(max_length=1024)

    def __str__(self):
        return self.name
    
    def get_tags(self):
        return self.tags.split(',')
    

class TrajElement(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    tags = models.CharField(max_length=1024)
    trajectory = models.ForeignKey(Trajectory, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):  
        return self.name
    
    def get_tags(self):
        return self.tags.split(',')
    
