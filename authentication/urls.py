from django.urls import path,include
from authentication import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('reg/', views.register, name="reg"),
    path('accounts/', include('django.contrib.auth.urls')),
]


