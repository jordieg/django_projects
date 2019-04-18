from django.db import models

# Create your models here.
class Category(models.Model) :
	name = models.CharField(max_length=128, null=True) 						# Category 

	def __str__(self):
		return self.name

class Iso(models.Model) :
        name = models.CharField(max_length=2, null=True)                                

        def __str__(self):
                return self.name

class Region(models.Model) :
        name = models.CharField(max_length=128, null=True)
        latitude = models.DecimalField(decimal_places=10, max_digits=22, null=True)                                               # Longitude
        longitude = models.DecimalField(decimal_places=10, max_digits=22, null=True)                                              # Latitude 

        def __str__(self):
                return self.name

class States(models.Model):
        name = models.CharField(max_length=128, null=True)							# State
        iso = models.ForeignKey(Iso, on_delete=models.CASCADE, null=True)			# iso
        region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)	# region
        
        def __str__(self):
                return self.name

class Site(models.Model):
	name = models.CharField(max_length=128, null=True) 						# Name
	description = models.CharField(max_length=128, null=True)							# Description
	justification = models.CharField(max_length=128, null=True) 							# Justification
	year = models.IntegerField(null=True)							# year
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	states = models.ForeignKey(States, on_delete=models.CASCADE, null=True)
	area_hectares = models.DecimalField(decimal_places=10, max_digits=22, null=True)						# area_hectares


	def __str__(self):
		return self.name



