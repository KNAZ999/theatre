from django.db import models
from django.contrib.admin import display
from django.urls import reverse
from django.db.models import functions


class Play(models.Model):
    title = models.CharField(max_length=255)
    annotations = models.TextField()

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.name


class ShowManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(starts_at__gte=functions.Now())

    def get_queryset(self):
        return super().get_queryset()


class Show(models.Model):
    starts_at = models.DateTimeField()
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor)

    objects = ShowManager()

    @display
    def play_name(self):
        return self.play.title

    def get_absolute_url(self):
        return reverse("plays:show_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.play.title} — {self.starts_at}"