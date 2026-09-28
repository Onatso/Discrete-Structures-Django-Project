from django.urls import path
from .views import user_page_view
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path("self_page/",user_page_view,name = "user_page")
]

