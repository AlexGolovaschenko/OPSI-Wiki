from django import forms
from partners.models import Contractor, Supplier

class ContractorUpdateForm (forms.ModelForm):
	class Meta:
		model = Contractor
		fields = '__all__'


class SupplierUpdateForm (forms.ModelForm):
	class Meta:
		model = Supplier
		fields = '__all__'