from django.db import models


# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    team_city = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    player_name = models.CharField(max_length=200)
    begin_date = models.DateField('date attend')

    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_name

# def was_published_recently(self):
# return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
