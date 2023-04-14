from django import forms
from .models import Disease, Pain

class PainDiseaseForm(forms.Form):
    pain = forms.ModelMultipleChoiceField(queryset=Pain.objects.all())
    disease = forms.ModelMultipleChoiceField(queryset=Disease.objects.all())
