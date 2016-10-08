from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal, User
from .forms import GoalForm, UserForm

# Create your views here.
def front_site(request):
    if request.method == "POST":
        goal_form = GoalForm(request.POST)
        if all([goal_form.is_valid()]):
            goal = goal_form.save(commit="False")
            goal.save()
            return redirect('add_info', pk=goal.pk)
        else:
            goal_form = GoalForm(request.POST)
            return render(request, 'goalapp/front_site.html',  {'goal_form': goal_form})
    else:
        goal_form = GoalForm()
        return render(request, 'goalapp/front_site.html',  {'goal_form': goal_form})

def user_goals(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'goalapp/user_goals.html', {'user': user})

def add_info(request, pk):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        goal = get_object_or_404(Goal, pk=pk)
        if all([user_form.is_valid()]):
            user = user_form.save(commit="False")
            goal.user = user
            user.save()
            goal.save()
            return redirect('user_goals', pk=user.pk)
        else:
            user_form = UserForm(request.POST)
            return render(request, 'goalapp/front_site.html',  {'user_form': user_form, 'goal_form': goal_form})
    else:
        goal = get_object_or_404(Goal, pk=pk)
        user_form = UserForm()
        return render(request, 'goalapp/add_info.html',  {'user_form': user_form, 'goal': goal})
