from django.db import models

# Create your models here.

class City(models.Model):
    city_name = models.CharField(max_length=20, default="Nombre de la ciudad")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.city_name
    
class Team(models.Model):
    venue = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    team_name = models.CharField(max_length=50, default="Nombre del equipo")
    players = models.IntegerField(default=0)
    director = models.CharField(max_length=30, default="Director a cargo")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.team_name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=50, default="Nombre del jugador")
    number = models.IntegerField(default=0)
    position = models.CharField(max_length=30, default="Posicion del jugador")

    def __str__(self):
        return self.player_name

class Stadium(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    stadium_name = models.CharField(max_length=50, default="Nombre del estadio")
    capacity = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.stadium_name
