from django.shortcuts import render
from .models import Goal
from .forms import GoalForm

# Create your views here.
def front_site(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            post= form.save(commit=True)
            return render(request, 'goalapp/front_site.html',  {'form': form})
    else:
        form=GoalForm()
        return render(request, 'goalapp/front_site.html',  {'form': form})
