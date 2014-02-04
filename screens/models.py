from django.db import models
from django.contrib.auth.models import User

#-------------------------------------------------------------------------------
class Screen(models.Model):
	screen_name		=	models.CharField(max_length=50)
	well			=	models.CharField(max_length=5)
	buffer			=	models.CharField(max_length=100, blank=True)
	salt1			=	models.CharField(max_length=100, blank=True)
	salt2			=	models.CharField(max_length=100, blank=True)
	salt3			=	models.CharField(max_length=100, blank=True)
	salt4			=	models.CharField(max_length=100, blank=True)
	prec1			=	models.CharField(max_length=100, blank=True)
	prec2			=	models.CharField(max_length=100, blank=True)
	prec3			=	models.CharField(max_length=100, blank=True)
	screen_ph		=	models.CharField(max_length=10, blank=True)
	#categories  = models.ManyToManyField(Category, related_name="packages")
	def __str__(self):
		return self.screen_name

	class Meta:
		ordering = ("screen_name","buffer",)

	class Admin:
		list_display = ('screen_name', 'well', 'buffer','salt1','salt2','prec1','prec2','screen_ph')
		search_fields = ('screen_name', 'buffer', 'salt1')


#-------------------------------------------------------------------------------
class Experiment(models.Model):
	experiment_name		=	models.CharField(max_length=50)
	description			=	models.TextField(max_length=300)
	date_started		=	models.DateField()
	num_plates			=	models.PositiveIntegerField()
	user				=	models.ForeignKey(User)
	
	#categories  = models.ManyToManyField(Category, related_name="packages")
	def __str__(self):
		return self.experiment_name

	class Meta:
		ordering = ["experiment_name","user"]

	class Admin:
		list_display = ('experiment_name', 'date_started')
		search_fields = ('experiment_name','description')

#-------------------------------------------------------------------------------
class Plate(models.Model):
	name			=	models.CharField(max_length=50)
	date_setup		=	models.DateField()
	experiment		=	models.ForeignKey(Experiment)
	screen			= 	models.ManyToManyField(Screen, related_name="screen")
	def __str__(self):
		return self.name

	class Meta:
		ordering = ("name",)

	class Admin:
		pass

	def set_screen_name(self, sname):
		pass	


#-------------------------------------------------------------------------------
class Photo(models.Model):
	well			=	models.CharField(max_length=4)
	screen_well		=	models.ForeignKey(Screen)
	plate 			=	models.ForeignKey(Plate)
	
	def __str__(self):
		return self.name

	class Meta:
		pass

	class Admin:
		pass

	def set_screen_name(self, sname):
		pass	
