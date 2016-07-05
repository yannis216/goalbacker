from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal, User
from .forms import GoalForm, UserForm

# Create your views here.
def front_site(request):
    if request.method == "POST":
        goal_form = GoalForm(request.POST)
        user_form = UserForm(request.POST)
        if all([goal_form.is_valid(), user_form.is_valid()]):
            user = user_form.save()
            goal = goal_form.save(commit="False")
            goal.user = user
            goal.save()
            return redirect('user_goals' , pk=user.pk)
        else:
            user_form = UserForm(request.POST)
            goal_form = GoalForm(request.POST)
            return render(request, 'goalapp/front_site.html',  {'user_form': user_form, 'goal_form': goal_form})
    else:
        goal_form = GoalForm()
        user_form = UserForm()
        return render(request, 'goalapp/front_site.html',  {'user_form': user_form, 'goal_form': goal_form})

def user_goals(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'goalapp/user_goals.html', {'user': user})
