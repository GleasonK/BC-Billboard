from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
import datetime, os
from PIL import Image as PImage
## Need do download Pillow for image handling
#  http://python-imaging.github.io/Pillow/

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

class Image(models.Model):
	image = models.ImageField(upload_to='images/%Y/%m', null=False, blank=False)
	albums = models.ManyToManyField(Album, blank=True)
	##Add facebook event link? Add location field?
	##Separate based on ForeignKey(Event) / ForeignKey(Image)
	# auto
	#attending = models.ManyToManyField(Attending)

	##Enter Size (ex: "m") to get the path to that photo
	def get_image_path(self, size=''):
		return os.sep.join([
			os.path.dirname(self.image.path),
			self.get_image_filename(size)
		])

	## Get the path to the directory
	def get_image_dir(self):
		return os.path.dirname(self.image.path)

	## Get the image url ("media/images/...")
	def get_image_url(self):
		return self.image.url

	##Get the location name for HMTL ("images/%Y/%m/...")
	def get_image_file_loc(self):
		return self.image.name

	## If empty (first call) return the absolute path to image
	## When calling for size, return with 'size'_'file'.jpg
	def get_image_filename(self, size=''):
		if size != '':
			return '_'.join([size,os.path.basename(self.image.path)])
		else:
			return ''.join([size,os.path.basename(self.image.path)])

	def get_medium_filename(self):
		return self.get_image_path("m")
		#return str(os.path.basename(self.image.path))
	## Make a save function that saves the file as well as a small version
	## of the file
	def save(self):
		super(Image,self).save()
		filename = self.get_image_path()
		# filename = self.get_image_filename()
		if not filename == '':
			img = PImage.open(filename)
			img.thumbnail((500,500), PImage.ANTIALIAS)
			img.save(self.get_medium_filename())

	def delete(self):
		filename = self.get_image_filename()
		try:
			os.remove(self.get_medium_filename())
		except:
			pass
		super(Image, self).delete()

	def thumbnail(self):
		return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a> """ % (
			(self.image.name, self.image.name))
	thumbnail.allow_tags = True

	
class Attending(models.Model):
	user = models.ForeignKey(User)
	#image = models.ForeignKey(Image)

	## Need unicode so it only adds user name and not user object
	def __unicode__(self):
		return unicode(self.user)

class Event(models.Model):
	title = models.CharField(max_length=60, null=False, blank = False)
	image = models.ForeignKey(Image, blank=False)
	eDate = models.DateTimeField()
	tags = models.ManyToManyField(Tag, blank=True)
	description = models.TextField()
	user = models.ForeignKey(User, null=False, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)
	attending = models.ManyToManyField(Attending, blank=True)

	def album_(self):
		return '\n'.join([a.title for a in self.albums.all()])

	def tags_(self):
		return '\n'.join([t.tag for t in self.tags.all()])

	def attending_(self):
		return '\n'.join([at.user for at in self.attending.all()])

	def is_upcoming_event(self):
		'''
		Return whether event is occuring within a month from current date
		'''
		now = timezone.now()
		return now - datetime.timedelta(hours = 3) <= self.eDate < now + datetime.timedelta(days=30)
	is_upcoming_event.admin_order_field = 'eDate'
	is_upcoming_event.boolean = True
	is_upcoming_event.short_description = 'UE?'

	def __unicode__(self):
		return self.title

