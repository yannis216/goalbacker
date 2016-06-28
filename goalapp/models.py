from django.db import models
from django.utils import timezone

class Goal(models.Model):
    goal_setter = models.CharField(max_length=50)
    goal_body = models.CharField(max_length= 100)
    goal_deadline = models.DateTimeField(default=timezone.now)




    def __str__(self):
        return self.goal_body
