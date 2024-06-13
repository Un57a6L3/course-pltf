import django_tables2 as tables
from .models import TrajElement, Course

class CourseTable(tables.Table):
    name = tables.Column(verbose_name='Название курса')
    topic = tables.Column(verbose_name='Тема')
    language = tables.Column(verbose_name='Язык')
    duration = tables.Column(verbose_name='Длительность (ч)')
    difficulty = tables.Column(verbose_name='Сложность')
    detail = tables.Column(verbose_name='Подробность')
    userscore = tables.Column(verbose_name='Рейтинг')

    class Meta:
        model = Course
        fields=['name', 'topic', 'language', 'duration', 'difficulty', 'detail', 'userscore']
        order_by = '-userscore'
        attrs = {'class': 'table table-dark table-striped'}
