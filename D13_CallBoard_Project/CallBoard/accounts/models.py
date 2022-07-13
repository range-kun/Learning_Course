from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    HUMAN = 'HUM'
    ORC = 'ORC'
    UNDEAD = 'UND'
    NIGHT_ELVES = 'NIE'
    races = [(HUMAN, 'Человек'), (ORC, 'Орк'),
             (UNDEAD, 'Нежеть'), (NIGHT_ELVES, 'Ночные эльфы')]

    race = models.CharField(max_length=3, choices=races, default=HUMAN)

    def __str__(self):
        return self.username
