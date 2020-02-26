from django.urls import path
from djangoApp import views

urlpatterns = [
	path('home/', views.home),
	path('addpost/',views.addpost,name='addpost'),
	path('showpost/<num>/',views.details,name='showpost'),
	path('sportsCat/',views.sportsCat,name='sportsCat'),
	path('foodCat/',views.foodCat,name='foodCat'),
	path('booksCat/',views.booksCat,name='booksCat'),
	path('likes/<num>/',views.likes),
	path('adduser/',views.adduser,name='adduser'),
	# path('',views.comments)
]