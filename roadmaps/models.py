from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


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
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=50, default='student')
    completed_elements = models.ManyToManyField(TrajElement)

    def __str__(self):
        return self.user.username


@receiver(pre_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    if not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
