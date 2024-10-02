from django.db import models

# Create your models here.


class City(models.Model):

    name = models.CharField('Название города', max_length=100)


class News(models.Model):
    title = models.CharField('Заголовок новости', max_length=100)
    content = models.TextField('Содержание новости')
    publication_date = models.DateTimeField('Дата публикации')
    author = models.CharField('Автор новости', max_length=100)
    city = models.ForeignKey('City', verbose_name='Город', on_delete=models.CASCADE, related_name='news')


class CityManagement(models.Model):
    fio = models.CharField('ФИО управляющего', max_length=256)
    city = models.ForeignKey('City', verbose_name='Город', on_delete=models.CASCADE)
    position = models.ForeignKey('PositionManagers', verbose_name='Должность', on_delete=models.CASCADE)


class PositionManagers(models.Model):
    position = models.CharField('Должность', max_length=256)
    salary = models.IntegerField('Зарплата')
    city = models.ForeignKey('City', verbose_name='Город', on_delete=models.CASCADE)
    date_start = models.DateField('Дата начала работы')
    date_end = models.DateField('Дата конца работы', blank=True, null=True)


class FactsCity(models.Model):
    name = models.CharField('название факта', max_length=128)
    text = models.TextField('Описание факта')

class Contacts(models.Model):
    phone = models.CharField('Телефон', max_length=15)
    email = models.EmailField('Электронная почта')
    city = models.ForeignKey('City', verbose_name='Город', on_delete=models.CASCADE)
    title = models.CharField('Служба', max_length=128)
