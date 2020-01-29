from django import forms
from partners.models import Contractor, Supplier

class ContractorUpdateForm (forms.ModelForm):
	rating = forms.IntegerField(min_value=0, max_value=5, required=True, label='Оценка', help_text='Значение от 0 до 5')

	class Meta:
		model = Contractor
		fields = '__all__'


class SupplierUpdateForm (forms.ModelForm):
	rating = forms.IntegerField(min_value=0, max_value=5, required=True, label='Оценка', help_text='Значение от 0 до 5')

	class Meta:
		model = Supplier
		fields = '__all__'
