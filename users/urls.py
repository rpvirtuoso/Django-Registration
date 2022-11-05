from django.urls import path
from .views import home, signup, login_user, logout_user, change_password

urlpatterns = [path('home', home, name='home'),
               path('signup', signup, name='signup'),
               path('login', login_user, name='login'),
               path('logout', logout_user, name='logout'),
               path('change-password', change_password, name='change-password')]
