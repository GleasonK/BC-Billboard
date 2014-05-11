from django import forms
from models import Event


class EventForm(forms.ModelForm):

	class Meta:
		## Bind to Event model
		model = Event

		## Display Fields:
		fields = ('title', 'image', 'eDate', 'tags', 'description')