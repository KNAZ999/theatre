from django.db import models
from django.contrib.admin import display
from django.db.models import functions

from users.models import User

# Create your models here.
class Play(models.Model):
    title = models.CharField(max_length=255)
    annotations = models.TextField()


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True)


class ShowManager(models.Manager):
    def active(self):
        self.get_queryset().filter(starts_at__gt=functions.Now())


class Show(models.Model):
    starts_at = models.DateTimeField()
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)

    objects = ShowManager()

    @display
    def play_name(self):
        return self.play.title


class Booking(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Бронь {self.seats} мест — {self.show}"