from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    date = models.DateField(verbose_name='Дата')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    distance = models.PositiveIntegerField(verbose_name='Расстояние')

    class Meta:
        verbose_name = 'таблица'
        verbose_name_plural = 'Таблица'

    def __str__(self):
        return self.name
