from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=100)
    duration = models.IntegerField()
    cast = models.ManyToManyField(Person, through='CastMembers')

    def __str__(self):
        return self.title


class CastMembers(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=64)