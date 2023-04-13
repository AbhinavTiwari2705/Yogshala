from django.shortcuts import render
from .models import yoga
from .forms import PainDiseaseForm


# Create your views here.

def home(request):
    return render(request, 'landing.html')


def suggest_yoga(request):
    if request.method == 'POST':
        form = PainDiseaseForm(request.POST)
        if form.is_valid():
            selected_pains = form.cleaned_data['pain']
            selected_diseases = form.cleaned_data['disease']
            suggested_yoga = yoga.objects.filter(Pain__in=selected_pains, Disease__in=selected_diseases)
            return render(request, 'suggested_yoga.html', {'suggested_yoga': suggested_yoga})
    else:
        form = PainDiseaseForm()
    return render(request, 'pain_disease_form.html', {'form': form})
