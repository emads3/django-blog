from django.shortcuts import render, redirect
# from .models import Post,post_likes,Forbidden_Words
from django.http import HttpResponse ,  HttpResponseRedirect

# Create your views here.


def adminPanel(request):
	context={}
	return render(request,'djangoApp/index.html/',context)

#Posts
def posts_table(request):
	# all_posts = Post.objects.all()
	# context = {'all_posts':all_posts}
	return render(request,'djangoApp/posts_table.html/')

# def addpost(request):
# 	post_form=postForm()  # hna ha3ml call lel form bta3t el post
# 	if request.method == "POST":
# 		post_form=postForm(request.POST)
# 		if post_form.is_valid():
# 			post_form.save()
# 			return HttpResponseRedirect('' )  #path of addpost.html 

# 	else:
# 		context={'post_form':post_form}
# 		return render(request,'#',context)   #path of addpost.html 

# def deletepost(request,num):
# 	obj = Post.objects.get(id = num)
# 	obj.delete()
# 	return HttpResponseRedirect('#') #path of deletepost.html

#Users
def users_table(request):
	#all_Users= User.objects.all()
	#context = {'all_Users':all_Users}
	return render(request,'/djangoApp/users_table.html/')


# def adduser(request):
# 	user_form=userForm()
# 	if request.method == "POST":
# 		user_form=userForm(request.POST)
# 		if user_form.is_valid():
# 			user_form.save()
# 			return HttpResponseRedirect('#') #path of adduser.html

# 	else:
# 		context={'user_Form':user_form}
# 		return render(request,'#',context) #path of adduser.html

# def deleteuser(request,num):
# 	obj = user.objects.get(id = num)
# 	obj.delete()
# 	return HttpResponseRedirect('#') #path of deleteuser.html

# #categories
def categories_table(request):
	#categories= categories.objects.all()  #categories!!
	#context = {'categories':categories}
	return render(request,'djangoApp/categories_table.html/')  

# def addcategory(request):
# 	category_form=StudentForm()
# 	if request.method == "POST":
# 		category_form=categoryForm(request.POST)
# 		if category_form.is_valid():
# 			category_form.save()
# 			return HttpResponseRedirect('#') #path of addcategory.html
# 	else:
# 		context={'category_Form':st_form}
# 		return render(request,'#',context)  #path of addcategory.html

# def deletecategory(request,num):
# 	obj = category.objects.get(id = num)
# 	obj.delete()
# 	return HttpResponseRedirect('#')  #path of deletecategory.html

# forbbidden_words
def forbidden_words_table(request):
	#all_forbbidden_words= Forbidden_Words.objects.all()
	#context = {'forbidden_words':all_forbidden_words}
	return render(request,'djangoApp/forbidden_words_table.html/')


# def addforbbiddenWord(request):
# 	forbbiddenWords_form=forbbiddenWordsForm()
# 	if request.method == "POST":
# 		forbbiddenWords_form=forbbiddenWordsForm(request.POST)
# 		if forbbiddenWords_form.is_valid():
# 			forbbiddenWords_form.save()
# 			return HttpResponseRedirect('#')  #path of addforbbiddenWord.html
# 	else:
# 		context={'forbbiddenWords_Form':st_form}
# 		return render(request,'#',context)  #path of addforbbiddenWord.html

# def deleteforbbiddenWord(request,num):
# 	obj =  Forbidden_Words.objects.get(id = num)
# 	obj.delete()
# 	return HttpResponseRedirect('#')   #path of deleteforbbiddenWord.html


# def register(request):
# 	return render(request,'djangoApp/register.html')


# def login(request):
# 	return render(request,'djangoApp/login.html')


