from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from img_upload.models import
from img_upload.models import Image, Tag, Attending



# Create your views here.
class IndexView(generic.ListView):
	template_name = 'img_upload/index1.html'
	context_object_name = 'recent_images' #this names the list of things that will be sent to the html from this view

	def get_queryset(self):
		"""Return the most recent 5 uploaded images"""
		return Image.objects[:2]
		#filter(eDate__gte= timezone.now()).order_by('-eDate')

