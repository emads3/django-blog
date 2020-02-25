from django.shortcuts import render
from localApp.models import Users,Categories,Posts,Comments,Tags,Post_Tags,Forbidden_Words,Post_Likes_Dislikes
from django.http import HttpResponse,HttpResponseRedirect
from localApp.forms import PostForm,UserForm

def home(request):
	latest_post_list = Posts.objects.all()
	context = {'latest_post_list' : latest_post_list}
	return render(request,'localApp/home.html',context)

def details(request,num):
	post = Posts.objects.get(id = num)
	context = { 'post_obj':post }
	return render(request,'localApp/details.html',context)


def addpost(request):
	if request.method == 'POST':
		post_form = PostForm(request.POST)
		if post_form.is_valid():
			post_form.save()
			return HttpResponseRedirect('/localApp/home')
	else:
		post_form = PostForm()
		context = { 'post_form':post_form }
		return render(request , 'localApp/post_add.html' , context)

def sportsCat(request):
	sports_cat = Posts.objects.filter(cat = 1)
	context = { 'sports_cat':sports_cat }
	return render(request , 'localApp/sports_cat.html' , context)

def foodCat(request):
	food_cat = Posts.objects.filter(cat = 2)
	context = { 'food_cat':food_cat }
	return render(request , 'localApp/food_cat.html' , context)

def booksCat(request):
	books_cat = Posts.objects.filter(cat = 3)
	context = { 'books_cat':books_cat }
	return render(request , 'localApp/books_cat.html' , context)

def likes(request,num):
	post = Post_Likes_Dislikes.objects.get(post = num)
	post.likes += 1
	post_likes = post.save()
	context = { 'post_likes':post_likes }
	return render(request , '/localApp/home.html' ,context)

def adduser(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect('/localApp/home')
	else:
		user_form = UserForm()
		context = { 'user_form':user_form }
		return render(request , 'localApp/user_add.html' , context)