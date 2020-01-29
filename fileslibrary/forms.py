from django import forms
from fileslibrary.models import File, Topic


class FileAddForm(forms.ModelForm):
	class Meta():
		model = File
		fields = '__all__'
			

class TopicAddForm(forms.ModelForm):
	class Meta():
		model = Topic
		fields = '__all__'