from django import forms
from .models import Goal, User, Funder

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('goal_body', 'goal_deadline')

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ('user', 'user_email')

class MoneyForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('goal_funds',)

class UserFundForm(forms.ModelForm):
    class Meta:
        model= Funder
        fields = ('funder', 'funder_email')
