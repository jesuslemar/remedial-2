from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('', views.Inicio.as_view(), name="inicio"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]