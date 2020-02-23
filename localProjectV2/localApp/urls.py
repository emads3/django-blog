from django.urls import path
from localApp import views

urlpatterns = [
	path('home/', views.home),
	path('addpost/',views.addpost),
	path('showpost/<num>',views.details),
	# path('sportsCat',views.sportsCat)
]