from django.urls import path,include
from djangoApp import views

urlpatterns = [
		path('index/',views.adminPanel),
		path('base/',views.base),


		path('posts_table/',views.posts_table , name='posts_table'),
	    #path('addpost', views.addpost), 
		# path('deletepost/<num>', views.deletepost),

		path('users_table/',views.users_table , name='users_table'),
		# path('adduser', views.adduser),  #page el login
		# path('deleteuser/<num>', views.deleteuser), #mogarad query fel database
		# path('edituser/<num>', views.edituser),  #el form h3dl el field bt3 is_active w 
		
		path('categories_table/',views.categories_table , name='categories_table'),
		# path('addcategory', views.addcategory),   #page el category
		# path('deletecategory/<num>', views.deletecategory),  #mogarad query fel database

		path('forbiden_words_table/',views.forbiden_words_table,name='forbiden_words_table'),
		path('addforbbiddenWord/', views.addforbbiddenWord , name='addforbbiddenWord'),  #form to add  forbidden word
		# path('deleteforbbiddenWord/<num>', views.deleteforbbiddenWord),  #mogarad query fel database

		# path('register/',views.register),
		# path('login/',views.login),

	]
		
