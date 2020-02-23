from django.urls import path,include
from djangoApp import views

urlpatterns = [
		path('index/',views.adminPanel),

		path('posts_table/',views.posts_table),
	 #    path('addpost', views.addpost), 
		# path('deletepost/<num>', views.deletepost),

		path('users_table/',views.users_table),
		# path('adduser', views.adduser), 
		# path('deleteuser/<num>', views.deleteuser),

		path('categories_table/',views.categories_table),
		# path('addcategory', views.addcategory), 
		# path('deletecategory/<num>', views.deletecategory),

		path('forbiden_words_table/',views.forbidden_words_table),
		# path('addforbbiddenWord', views.addforbbiddenWord), 
		# path('deleteforbbiddenWord/<num>', views.deleteforbbiddenWord),

		# path('register/',views.register),
		# path('login/',views.login),

	]
		
