from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def user_page_view(request):
    return render(request,"sign/user_page.html",{})

