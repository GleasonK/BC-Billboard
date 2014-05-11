from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.core.context_processors import csrf
from img_upload.models import Image, Tag, Attending, Event
from forms import EventForm



#Create your views here.
class IndexView(generic.ListView):
	template_name = 'img_upload/index.html'
	context_object_name = 'recent_images'
	#Names the list of things that will be sent to the html from this view

	def get_queryset(self):
		"""Return the most recent uploaded images"""
		return Event.objects.filter(eDate__gte= timezone.now()).order_by('-eDate')

	def get_context_data(self, **kwargs):
			# Call the base implementation first to get a context
			context = super(IndexView, self).get_context_data(**kwargs)
			# Add in a QuerySet of all the books
			context['pageHeader'] = 'Testing Upload Properties'
			return context

def create_event(request):
	# Returns false on empty
	if request.POST:
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('')
	else:
		form = EventForm

	## Page Context Arguments
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render(request, 'img_upload/create_event.html', args)
