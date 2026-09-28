from django.db import models
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

# Create your models here.


class StduentSignupForm(SignupForm):
    def save(self, request):
        user = super(StduentSignupForm,self).save(request)
        student_group = Group.objects.get(name = "Students")
        student_group.user_set.add(user)
        return user
