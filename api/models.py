from django.db import models


class Dog(models.Model):
	GENDER_CHOICES = [
		("F", "Female"),
		("M", "Male")
	]
	
	name = models.CharField(max_length= 50)
	age = models.IntegerField(default= 0)
	breed = models.ForeignKey("Breed", on_delete= models.CASCADE, related_name= "breed")
	gender = models.CharField(max_length= 1, choices= GENDER_CHOICES, default= "M")
	color = models.CharField(max_length= 60)
	favorite_food = models.CharField(max_length= 50, verbose_name= "Favorite food")
	favorite_toy = models.CharField(max_length= 50, verbose_name= "Favorite toy")
	
	
	def __str__(self):
		return self.name
		
		
class Breed(models.Model):
	SIZE_CHOICES = [
		("Tiny", "Tiny"),
		("Small", "Small"),
		("Medium", "Medium"),
		("Large", "Large")
	]
	
	FRIENDLINESS_CHOICES = [
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5)
	]
	
	TRAINABILITY_CHOICES = [
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5)
	]
	
	EXERCISE_CHOICES = [
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5)
	]
	
	name = models.CharField(max_length= 50)
	size = models.CharField(max_length= 6, choices= SIZE_CHOICES, default= "Small")
	friendliness = models.IntegerField(choices= FRIENDLINESS_CHOICES, default= 5)
	trainability = models.IntegerField(choices= TRAINABILITY_CHOICES, default= 5)
	exerciseneeds = models.IntegerField(choices= EXERCISE_CHOICES, default= 5, verbose_name= "Exercise needs")
	
	def __str__(self):
		return self.name
		
		
		