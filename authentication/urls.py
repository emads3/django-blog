from django.urls import path,include
from authentication import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
]


