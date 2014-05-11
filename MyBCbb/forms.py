from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import SelectMultiple


class MyRegistrationForm(UserCreationForm):
	## Tell what parts of information you want to pull from format
	## Define a field
	MAJOR_CHOICES = ("Art History", "Biochemistry", "Biology", "Chemistry",
		"Classical Studies", "Communication", "Computer Science", 
		"Environmental Sciences", "Economics", "English", "Environmental Geoscience",
		"Environmental Studies", "Film Studies", "French", "Geological Sciences",
		"German Studies", "Hispanic Studies", "History", "Independent Study",
		"International Studies", "Islamic Civilization and Societies", "Italian",
		"Linguistics", "Mathematics", "Music", "Philosophy", "Physics", 
		"Political Science", "Psychology", "Russian", "Slavic Studies", "Sociology",
		"Studio Art", "Theater", "Theology")



	email = forms.EmailField(required=True)
	fName = forms.CharField(label = "First Name", required=True)
	lName = forms.CharField(label = "Last Name" ,required=True)
	major = forms.MultipleChoiceField(required=False,
		widget=SelectMultiple, choices=MAJOR_CHOICES)

	class Meta:
		model = User
		fields = ('username', 'fName', 'lName', 'email', 'password1', 'password2')

	##Overwrite the UCF save function
	def save(self, commit=True):
		## False since we dont want to save right away, need to edit
		## If inherited elsewhere must spcify whether we want auto save
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['fName']
		user.last_name = self.cleaned_data['lName']
		user.major = self.cleaned_data['major']

		if commit:
			user.save()

		return user