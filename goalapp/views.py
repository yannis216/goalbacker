from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal, User
from .forms import GoalForm, UserForm, MoneyForm, UserFundForm

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

def add_info(request, pk):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        goal = get_object_or_404(Goal, pk=pk)
        if all([user_form.is_valid()]):
            user = user_form.save(commit="False")
            goal.user = user
            user.save()
            goal.save()
            return redirect('user_goals', pk=goal.pk)
        else:
            user_form = UserForm(request.POST)
            return render(request, 'goalapp/add_info.html',  {'user_form': user_form, 'goal_form': goal_form})
    else:
        goal = get_object_or_404(Goal, pk=pk)
        user_form = UserForm()
        return render(request, 'goalapp/add_info.html',  {'user_form': user_form, 'goal': goal})

def user_goals(request, pk):
    if request.method == "POST":
        money_form = MoneyForm(request.POST)
        goal = get_object_or_404(Goal, pk=pk)
        if all([money_form.is_valid()]):
            goal.goal_funds += int(money_form['goal_funds'].value())
            goal.save()
            return redirect('user_fund', pk=goal.pk)
        else:
            money_form = MoneyForm(request.POST)
            return render(request, 'goalapp/user_goals.html',  {'money_form': money_form})
    else:
        goal = get_object_or_404(Goal, pk=pk)
        money_form = MoneyForm()
        return render(request, 'goalapp/user_goals.html', {'goal': goal, 'money_form': money_form})


def user_fund(request, pk):
    if request.method =="POST":
        user_fund_form = UserFundForm(request.POST)
        goal = get_object_or_404(Goal, pk=pk)
        if all([user_fund_form.is_valid()]):
            funder = user_fund_form.save(commit="False")
            funder.funded_goal = goal
            funder.save()
            return redirect('user_goals', pk=goal.pk)

        else:
            user_fund_form = UserFundForm(request.POST)
            return render(request, 'goalapp/user_fund.html',  {'user_fund_form': user_fund_form})
    else:
        goal = get_object_or_404(Goal, pk=pk)
        user_fund_form = UserFundForm()
        return render(request, 'goalapp/user_fund.html',  {'user_fund_form': user_fund_form, 'goal': goal})
