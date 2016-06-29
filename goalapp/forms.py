from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('goal_setter', 'goal_body', 'goal_deadline')
