from django.db import models


# Create your models here.

class Team(models.Model):
<<<<<<< HEAD
    team_name = models.CharField(max_length=200)
    team_city = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    player_name = models.CharField(max_length=200)
    begin_date = models.DateField('date attend')

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
=======
	
	team_name = models.CharField(primary_key = True, max_length = 200)
	team_city = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.team_name

class Player(models.Model):
	player_name = models.CharField(primary_key = True, max_length = 200)
	begin_date = models.DateField('date been selected')
	
	team = models.ForeignKey(Team, on_delete = models.CASCADE)
>>>>>>> 8afd2e11426d3fdd3ba30c7d013a8f49e3681916

    def __str__(self):
        return self.player_name

# def was_published_recently(self):
# return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
