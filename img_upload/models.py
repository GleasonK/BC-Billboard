from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import PIL

# Create your models here.

class Tag(models.Model):
	tag = models.CharField(max_length=50, blank=True, null=True)
	def __unicode__(self):
		return self.tag

class Album(models.Model):
	title = models.CharField(max_length= 60)
	public = models.BooleanField(default=False)
	def __unicode__(self):
		return self.title

class Attending(models.Model):
	user = models.ForeignKey(User)
	image = models.ForeignKey(Image)
	def __unicode__(self):
		return self.user

class Image(models.Model):
	title = models.CharField(max_length=60, null=False, blank = False)
	eDate = models.DateTimeField()
	image = models.ImageField(upload_to='images/%Y/%m', null=False, blank=False)
	tags = models.ManyToManyField(Tag, blank=True)
	description = models.TextField()
	albums = models.ManyToManyField(Album, blank=True)

	def save(self):
		filename = self.get_image_filename()
		# filename = self.get_image_filename()
  #   if not filename == '':
  #       img = Image.open(filename)
  #       img.thumbnail((512,512), Image.ANTIALIAS)
  #       img.save(self.get_medium_filename())



	# auto
	attending = models.ManyToManyField(Attending)
	user = models.ForeignKey(User, null=False, blank=True)
	added = models.DateTimeField(auto_now_add=True)

