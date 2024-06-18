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

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name
    
    def get_tags(self):
        return self.tags.split(',')

    def get_absolute_url(self):
        return self.link


class Trajectory(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    description = models.TextField()
    tags = models.CharField(max_length=1024)

    class Meta:
        verbose_name = 'Траектория'
        verbose_name_plural = 'Траектории'

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

    class Meta:
        verbose_name = 'Элемент траектории'
        verbose_name_plural = 'Элементы траекторий'

    def __str__(self):  
        return self.name
    
    def get_tags(self):
        return self.tags.split(',')
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=50, default='student')
    completed_elements = models.ManyToManyField(TrajElement)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username
    
    def get_student_profiles(self):
        return Profile.objects.filter(role='student')
    
    def get_curated_groups(self):
        return self.curated_groups.all().order_by('name')
    
    def get_fullname(self):
        return f'{self.user.last_name} {self.user.first_name}'
    

class Group(models.Model):
    name = models.CharField(max_length=256)
    curators = models.ManyToManyField(Profile, related_name='curated_groups')
    participants = models.ManyToManyField(Profile, related_name='part_of_groups')
    trajectory = models.ForeignKey(Trajectory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name
    
    def get_students(self):
        return self.participants.filter(role='student')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    if not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Profile)
def manage_default_group(sender, instance, **kwargs):
    default_group = Group.objects.get(name='[Без группы]')
    if not instance.part_of_groups.exists():
        instance.part_of_groups.add(default_group)
    elif instance.part_of_groups.count() > 1 and default_group in instance.part_of_groups.all():
        instance.part_of_groups.remove(default_group)
