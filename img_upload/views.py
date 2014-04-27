from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
#from img_upload.models import
from img_upload.models import Image, Tag, Attending, Event



#Create your views here.
class IndexView(generic.ListView):
	template_name = 'img_upload/index1.php'
	context_object_name = 'recent_images'
	#Names the list of things that will be sent to the html from this view

	def get_queryset(self):
		"""Return the most recent uploaded images"""
		return Event.objects.filter(eDate__gte= timezone.now()).order_by('-eDate')

	def get_context_data(self, **kwargs):
			# Call the base implementation first to get a context
			context = super(IndexView, self).get_context_data(**kwargs)
			# Add in a QuerySet of all the books
			#context['identifier'] = "info"
			return context
