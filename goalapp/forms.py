from django import forms
from .models import Goal, User

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
