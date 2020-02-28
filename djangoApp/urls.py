from django.urls import path,include
from djangoApp import views

urlpatterns = [

		path('searchForPost', views.searchForPost , name='searchForPost'),
		# path('index/',views.adminPanel),
		path('admin/',views.admin,name='admin'),
		# path('home/', views.home),
		path('homepage/', views.home , name='homepage'),

		path('showpost/<num>/',views.showpost,name='showpost'),
		

  #------------------------------------------------------------------------------------------------------------
		#categories url
		path('categorypage/<name>',views.category,name='categorypage'),
		path('home/<num>',views.subscribe),

		#tags url
		path('tagpage/<name>',views.tagpage,name='tagpage'),
  #-------------------------------------------------------------------------------------------------------------
        #posts url

    	path('posts_table/',views.posts_table , name='posts_table'),
		path('addpost/', views.addpost , name='addpost'), 
		path('deletepost/<num>', views.deletepost , name='deletepost'),
		path('editpost/<num>',views.edit_post,name='editpost'),
		path('showpost/<postid>/addcomment',views.addcomment,name='addcomment'),
	
  #---------------------------------------------------------------------------------------------------------------
	   #user urls

		path('users_table/',views.users_table , name='users_table'),
		path('adduser', views.adduser , name='adduser'),  #page el login
		path('deleteuser/<num>', views.deleteuser , name='deleteuser'), #mogarad query fel database
		path('edituser/<num>', views.edituser , name='edituser'),  #el form h3dl el field bt3 is_active w 
  #-------------------------------------------------------------------------------------------------------------------
  		#categories urls

		path('categories_table/',views.categories_table , name='categories_table'),
		path('addcategory', views.addcategory , name='addcategory'),   #page el category
		path('deletecategory/<num>', views.deletecategory , name='deletecategory'),  #mogarad query fel database
		path('editcategory/<num>',views.editcategory,name='editcategory'),

 #-------------------------------------------------------------------------------------------------------------------
      #tag urls

      	path('tag_table/',views.tag_table , name='tag_table'),
		path('addtag/',views.addtag,name='addtag'),
		path('deletetag/<num>', views.deletetag, name='deletetag'),
		path('edittag/<num>',views.edittag,name='edittag'),
 #--------------------------------------------------------------------------------------------------------------------

        #hnmsa7hom dol el forbidden key
		path('forbiden_words_table/',views.forbiden_words_table,name='forbiden_words_table'),
		path('addword/', views.addforbbiddenword, name='addword'), 
		path('deleteword/<num>', views.deleteforbbiddenWord , name='deleteword'),
		path('editword/<num>',views.editforbbiddenword,name='editword'),
		# path('addforbbiddenword/', views.addforbbiddenword , name='addforbbiddenword'),  #form to add  forbidden word
		# path('deleteforbbiddenWord/<num>', views.deleteforbbiddenWord),  #mogarad query fel database

		# path('register/',views.register),
		# path('login/',views.login),

	]
		
