import django_tables2 as tables
from .models import TrajElement, Course

class CourseTable(tables.Table):
    class Meta:
        model = Course
        fields=['name', 'topic', 'language', 'duration', 'difficulty', 'detail', 'userscore']
        order_by = '-userscore'
