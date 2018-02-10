from django.forms import ModelForm


from .models import Participant


class ParticipantForm(ModelForm):
	class Meta:
		model = Participant
		fields = ('name', 'phone', 'email', 'allergies', 'program', 'grade')
		labels = {
			'name': 'Navn',
			'phone': 'Telefon', 
			'email': 'Epost', 
			'allergies': 'Allergier', 
			'program': 'Studie', 
			'grade': 'Trinn',
		}


	def __init__(self, *args, **kwargs):
		super(ParticipantForm, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
			'class': 'form-control'
			})