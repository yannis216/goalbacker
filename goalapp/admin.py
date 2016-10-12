from django.contrib import admin
from .models import Goal, User, Funder
# Register your models here.
admin.site.register(Goal)
admin.site.register(User)
admin.site.register(Funder)
