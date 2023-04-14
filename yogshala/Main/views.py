from django.shortcuts import render
from .models import yoga,Pain,Disease
from .forms import PainDiseaseForm
from django.db.models import Q


# Create your views here.

def home(request):
    return render(request, 'landing.html')


def suggest_yoga(request):
    if request.method == 'POST':
        form = PainDiseaseForm(request.POST)
        if form.is_valid():
            selected_pains = form.cleaned_data['pain']
            selected_diseases = form.cleaned_data['disease']
            suggested_yoga = yoga.objects.filter(Q(Pain__in=selected_pains) | Q(Disease__in=selected_diseases)).distinct()
            print(suggested_yoga)
            return render(request, 'suggested_yoga.html', {'suggested_yoga': suggested_yoga})
    else:
        form = PainDiseaseForm()
    return render(request, 'pain_disease_form.html', {'form': form})
