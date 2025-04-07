from django.urls import path
from app_home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    # path('logout', views.logout_view, name='logout'),
]
