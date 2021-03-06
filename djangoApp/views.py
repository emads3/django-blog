from django.shortcuts import render
from djangoApp.models import Users,Categories,Posts,Comments,Tags,Post_Tags,Forbidden_Words,Post_Likes_Dislikes
from django.http import HttpResponse,HttpResponseRedirect
from djangoApp.forms import PostForm,UserForm

def home(request):
	latest_post_list = Posts.objects.order_by('-post_date')[:5]
	context = {'latest_post_list' : latest_post_list}
	return render(request,'djangoApp/home.html',context)

def details(request,num):		#for when a user wants to see the details of a specific post
	post = Posts.objects.get(id = num)
	comment = Comments.objects.filter(post_id = num)
	likes_dislikes = Post_Likes_Dislikes.objects.filter(post = num)
	context = { 'post_obj':post , 
				'comment':comment ,
				'likes_dislikes':likes_dislikes }
	return render(request,'djangoApp/details.html',context)


def addpost(request):			#if a user wants to add a post
	if request.method == 'POST':
		post_form = PostForm(request.POST)
		if post_form.is_valid():
			post_form.save()
			return HttpResponseRedirect('/djangoApp/home')
	else:
		post_form = PostForm()
		context = { 'post_form':post_form }
		return render(request , 'djangoApp/post_add.html' , context)

def sportsCat(request):			#if the sports category button was pressed
	sports_cat = Posts.objects.filter(cat = 1)
	context = { 'sports_cat':sports_cat }
	return render(request , 'djangoApp/sports_cat.html' , context)

def foodCat(request):			#if the food category button was pressed
	food_cat = Posts.objects.filter(cat = 2)
	context = { 'food_cat':food_cat }
	return render(request , 'djangoApp/food_cat.html' , context)

def booksCat(request):			#if the food category button was pressed
	books_cat = Posts.objects.filter(cat = 3)
	context = { 'books_cat':books_cat }
	return render(request , 'djangoApp/books_cat.html' , context)

def likes(request,num):			#if the like button was pressed
	post = Post_Likes_Dislikes.objects.get(post = num)
	post.likes += 1
	post_likes = post.save()
	context = { 'post_likes':post_likes }
	return render(request , '/djangoApp/home.html' ,context)

def adduser(request):			#if the register button was pressed
	user_form = UserForm()		
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect('/djangoApp/home')
	else:
		user_form = UserForm()
		context = { 'user_form':user_form }
		return render(request , 'djangoApp/user_add.html' , context)

# def comments(request,num):
# 	comment = Comments.objects.filter(post_id = num)
# 	context = { 'comment':comment }
# 	return render(request,'djangoApp/details.html')