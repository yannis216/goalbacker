from django.db import models
from django.utils import timezone

class User(models.Model):
    user = models.CharField(max_length=50)
    user_email = models.EmailField()

    def __str__(self):
        return self.user

class Goal(models.Model):
    user = models.ForeignKey('goalapp.User', related_name='goal', on_delete=models.CASCADE, null=True)
    goal_body = models.CharField(max_length= 100)
    goal_deadline = models.DateTimeField(default=timezone.now)
    goal_status = models.IntegerField(default=1)

    def __str__(self):
        return self.goal_body
