from django.db import models
from datetime import date
from django.conf import settings
from django.urls import reverse


class Director(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    image = models.ImageField(upload_to='directors/', blank=False, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class Actor(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    image = models.ImageField(upload_to='actors/', blank=False, null=False)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Genre(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField('Название', max_length=255, blank=False, null=False)
    description = models.TextField('Описание')
    image = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2020)
    country = models.CharField('Страна', max_length=100)
    directors = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name='Режиссер')
    actors = models.ManyToManyField(Actor, verbose_name='Актеры')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    release_date = models.DateField('Премьера', default=date.today)

    def __str__(self):
        return f'{self.title} {self.release_date}'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Hall(models.Model):
    name = models.CharField(max_length=50)
    rows = models.PositiveSmallIntegerField()
    seats = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    free_seats = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.movie} - {self.start_time}'

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'


class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row_num = models.PositiveSmallIntegerField()
    seat_num = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.hall}: {self.row_num} ряд - {self.seat_num} место'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Booking(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    status_choices = [
        ('booked', 'Забронировано'),
        ('cancelled', 'Отменен'),
    ]
    status = models.CharField(max_length=10, choices=status_choices)
    booking_datetime = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.client} - {self.booking_datetime}'

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронь'