from django.db import models

# Create your models here.

class Team(models.Model):
<<<<<<< HEAD
=======
	
>>>>>>> b9133715603dc037a6f8adca1d12c877e029c87e
	team_name = models.CharField(primary_key = True, max_length = 200)
	team_city = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.team_name

class Player(models.Model):
<<<<<<< HEAD
    player_name = models.CharField(primary_key = True, max_length = 200)
    begin_date = models.DateField('date been selected')

    team = models.ForeignKey(Team, on_delete = models.CASCADE)

    def __str__(self): 
        return self.player_name
=======
	player_name = models.CharField(primary_key = True, max_length = 200)
	begin_date = models.DateField('date been selected')
	
	team = models.ForeignKey(Team, on_delete = models.CASCADE)

	def __str__(self):
		return self.player_name
>>>>>>> b9133715603dc037a6f8adca1d12c877e029c87e

	# def was_published_recently(self):
		# return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
		