from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import Disease, Pain


class PainDiseaseForm(forms.Form):
    pain = forms.ModelMultipleChoiceField(
        queryset=Pain.objects.all(),
        required=False,
        widget=CheckboxSelectMultiple(attrs={'class': 'form-group', 'id': 'pain'}),
    )
    
    disease = forms.ModelMultipleChoiceField(
        queryset=Disease.objects.all(),
        required=False,
        widget=CheckboxSelectMultiple(attrs={'class': 'form-group', 'id': 'disease'}),
    )
