from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
import datetime
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

	# auto
	attending = models.ManyToManyField(Attending)
	user = models.ForeignKey(User, null=False, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)

	def save(self):
		filename = self.get_image_filename()
		# filename = self.get_image_filename()
		if not filename == '':
			img = Image.open(filename)
			img.thumbnail((350,350), Image.ANTIALIAS)
			img.save(self.get_medium_filename())

	def is_upcoming_event(self):
		'''
		Return whether event is occuring within a month from current date
		'''
		now = timezone.now()
		return datetime.timedelta(hours = -3) <= self.eDate < datetime.timedelta(days=30)
	is_upcoming_event.admin_order_field = 'eDate'
	is_upcoming_event.boolean = True
	is_upcoming_event.short_description = 'Event Occurring Soon?'

	def __unicode__(self):
		return self.title
		



