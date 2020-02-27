
from django.shortcuts import render, redirect , get_object_or_404
from djangoApp.models import Categories,Post,Comments,Tag,post_likes
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from djangoApp.form import PostForm , CategoryForm , TagForm , UserForm


#--------------------------------------------------------------------------------------------------


#categories
# def sportsCat(request):			#if the sports category button was pressed
# 	sports_cat = Post.objects.filter(cat = 1)
# 	context = { 'sports_cat':sports_cat }
# 	return render(request,'djangoApp/marc/sports_cat.html/' , context)

# def foodCat(request):			#if the food category button was pressed
# 	food_cat = Post.objects.filter(cat = 2)
# 	context = { 'food_cat':food_cat }
# 	return render(request,'djangoApp/marc/food_cat.html/' , context)

# def booksCat(request):			#if the food category button was pressed
# 	books_cat = Post.objects.filter(cat = 3)
# 	context = { 'books_cat':books_cat }
# 	return render(request,'djangoApp/marc/books_cat.html' , context)

def category(request , name):
	obj=Categories.objects.get(cat_name = name)			#if the sports category button was pressed
	catposts = Post.objects.filter(cat = obj)
	all_categories=Categories.objects.all()
	all_tags=Tag.objects.all()

	context = { 'catposts':catposts ,
	            'all_categories' :all_categories ,
	             'all_tags':all_tags}
	return render(request , 'djangoApp/categorypage.html' ,context)



def tagpage(request , name):
	post_tag = Tag.objects.filter(name= name)

	all_posts=Post.objects.filter(id=post_tag)

	all_categories=Categories.objects.all()
	all_tags=Tag.objects.all()

	context = { 'all_posts':all_posts,
	            'all_categories' :all_categories ,
	             'all_tags':all_tags}
	return render(request , 'djangoApp/tagpage.html' ,context)


#-----------------------------------------------------------------------------------------------------

#admin panel


def admin(request):
	all_categories=Categories.objects.all()
	all_tags=Tag.objects.all()
	context={'all_categories':all_categories , 'all_tags':all_tags}
	# latest_post_list = Posts.objects.order_by('-post_date')[:5]
	# context = {'latest_post_list' : latest_post_list}
	return render(request,'djangoApp/adminpanel.html/',context)

def home(request):
	latest_post_list = Post.objects.order_by('-post_date')[:5]
	all_categories=Categories.objects.all()
	context = {'latest_post_list' : latest_post_list}
	return render(request,'djangoApp/homepage.html',context)


def showpost(request,num):		#for when a user wants to see the details of a specific post
	post = Post.objects.get(id = num)
	comment = Comments.objects.filter(post_id = num)
	likes_dislikes = post_likes.objects.filter(post = num)
	all_categories=Categories.objects.all()
	all_tags=Tag.objects.all()
	context = { 'post_obj':post , 
				'comment':comment ,
				'likes_dislikes':likes_dislikes,
				'all_categories' :all_categories ,
				 'all_tags':all_tags}
	return render(request,'djangoApp/showpost.html',context)


  #----------------------------------------------------------------

#Posts
def posts_table(request):
	all_posts = Post.objects.all()
	all_categories=Categories.objects.all()
	all_tags=Tag.objects.all()
	context = {'all_posts':all_posts,
	            'all_categories' :all_categories ,
	            'all_tags':all_tags}
	return render(request,'djangoApp/posts_table.html/',context)

def addpost(request):
	post_form = PostForm()			#if a user wants to add a post
	if request.method == 'POST':
		post_form = PostForm(request.POST,request.FILES)
		if post_form.is_valid():
			post_form.save()
			return redirect('/app/posts_table/')
	else:
		# post_form = PostForm()
		context = { 'post_form':post_form }
		return render(request , 'djangoApp/create.html/' , context)


def edit_post(request , num):
	post=get_object_or_404(Post,id=num)
	post_form=PostForm(instance=post)
	if request.method=='POST':
		post_form=PostForm(request.POST ,request.FILES, instance=post )
		if post_form.is_valid():
			post_form.save()
			return HttpResponseRedirect('/app/posts_table/')
	else:
		post_form=PostForm(instance=post)
		context={'post_form':post_form}
		return render(request,'djangoApp/editpost.html/',context)

def deletepost(request,num):
	obj = Post.objects.get(id = num)
	obj.delete()
	return HttpResponseRedirect('/app/posts_table/') #path of deletepost.html
   #------------------------------------------------------------------

#Users

def users_table(request):
	all_users= User.objects.all()
	all_categories=Categories.objects.all()
	all_tags=Tag.objects.all()
	context = {'all_users':all_users,
	             'all_categories' :all_categories ,
	             'all_tags':all_tags}
	return render(request,'djangoApp/users_table.html/',context)


def adduser(request):
	user_form=UserForm()
	if request.method == "POST":
		user_form=UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect('/app/users_table/') #path of adduser.html

	else:
		context={'user_form':user_form}
		return render(request,'djangoApp/adduser.html/',context) #path of adduser.html


def edituser(request,num):
	user = User.objects.get(id=num)
	user_form=UserForm(instance=user)
	if request.method == "POST":
		user_form=UserForm(request.POST , instance=user)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect('/app/users_table/')

	else:
		user_form=UserForm(instance=user)
		context={'user_form':user_form}
		return render(request,'djangoApp/adduser.html',context)

def deleteuser(request,num):
	obj = User.objects.get(id = num)
	obj.delete()
	return HttpResponseRedirect('/app/users_table/') #path of deleteuser.html

# def blocked(request,num):
# 	user=User.id
# 	user.is_active="True"
# 	return HttpResponseRedirect('djangoApp/users_table/')
 
#--------------------------------------------------------------------

# #categories

def categories_table(request):
	all_categories= Categories.objects.all()
	all_tags=Tag.objects.all()
	context = {'all_categories':all_categories , 'all_tags':all_tags}

	return render(request,'djangoApp/categories_table.html/',context)  

#-------------------------------------------------------------------------------
#subscribe

def subscribes(request, cat_id):
	print("ok")
	try:
		cat = category.objects.get(id = cat_id)
		subscribe.objects.create(user_id = request.user, cat_id = cat)
	finally:
		return HttpResponseRedirect('djangoApp/categories_table.html')

#------------------------------------------------------------------------
#unsubscribe

def unsubscribe(request, cat_id):
	# print("ok")
	try:
		cat = category.objects.get(id = cat_id)
		sub = subscribe.objects.get(user_id = request.user, cat_id = cat)
		sub.delete()
	finally:
		return HttpResponseRedirect('djangoApp/categories_table.html')

# def unsubscribe(request,cat_id):
#     try:
# 		cat = category.objects.get(id = cat_id)
# 		sub = subscribe.objects.get(user_id = request.user, cat_id = cat)
# 		sub.delete()
# 	finally:
# 		return HttpResponseRedirect('djangoApp/categories_table.html')

    
#-------------------------------------------------------------------------

def addcategory(request):
	category_form=CategoryForm()
	if request.method == "POST":
		category_form=CategoryForm(request.POST)
		if category_form.is_valid():
			category_form.save()
			return HttpResponseRedirect('/app/categories_table/') #path of addcategory.html
	else:
		context={'category_form':category_form}
		return render(request,'djangoApp/createcategory.html/',context)  #path of addcategory.html

def deletecategory(request,num):
	obj = Categories.objects.get(id = num)
	obj.delete()
	return HttpResponseRedirect('/app/categories_table/')  #path of deletecategory.html

def editcategory(request,num):
	category=get_object_or_404(Categories,id=num)
	category_form=CategoryForm(instance=category)
	if request.method == "POST":
		category_form=CategoryForm(request.POST,instance=category)
		if category_form.is_valid():
			category_form.save()
			return HttpResponseRedirect('/app/categories_table/')
	else:
		category_form=CategoryForm(instance=category)
		context={'category_form':category_form}
		return render(request,'djangoApp/createcategory.html/',context)


  #------------------------------------------------------------------
#Tag

def tag_table(request):
	all_tags= Tag.objects.all()  #categories!!
	all_categories=Categories.objects.all()
	context = {'all_tags':all_tags , 'all_categories' :all_categories}
	return render(request,'djangoApp/tag_table.html/',context)  

def addtag(request):
	tag_form=TagForm()
	if request.method == "POST":
		tag_form=TagForm(request.POST)
		if tag_form.is_valid():
			tag_form.save()
			return HttpResponseRedirect('/app/tag_table/') #path of addcategory.html
	else:
		context={'tag_form':tag_form}
		return render(request,'djangoApp/addtag.html/',context)  #path of addcategory.html


def deletetag(request,num):
	obj = Tag.objects.get(id = num)
	obj.delete()
	return HttpResponseRedirect('/app/tag_table/')  #path of deletecategory.html

def edittag(request,num):
	tag=get_object_or_404(Tag,id=num)
	tag_form=TagForm(instance=category)
	if request.method == "POST":
		tag_form=TagForm(request.POST,instance=tag)
		if tag_form.is_valid():
			tag_form.save()
			return HttpResponseRedirect('/app/tag_table/')
	else:
		tag_form=CategoryForm(instance=category)
		context={'tag_form':tag_form}
		return render(request,'djangoApp/addtag.html/',context)


  #----------------------------------------------------------------

# forbbidden_words

def forbiden_words_table(request):
	#all_forbbidden_words= Forbidden_Words.objects.all()
	all_categories=Categories.objects.all()
	all_tags=Tag.objects.all()
	context = {'all_categories' :all_categories , 'all_tags':all_tags}
	return render(request,'djangoApp/forbiden_words_table.html/' , context) 


# def addforbbiddenword(request):
# 	forbbiddenWords_form=ForbiddenForm()
# 	if request.method == "POST":
# 		forbbiddenWords_form=ForbiddenForm(request.POST)
# 		if forbbiddenWords_form.is_valid():
# 			forbbiddenWords_form.save()
# 			# return HttpResponseRedirect('#')  #path of addforbbiddenWord.html
# 	else:
# 		context={'forbbiddenWords_Form':forbbiddenWords_form}
# 		return render(request,'djangoApp/addforbiddenword.html/',context)  #path of addforbbiddenWord.html

# # def deleteforbbiddenWord(request,num):
# # 	obj =  Forbidden_Words.objects.get(id = num)
# # 	obj.delete()
# # 	return HttpResponseRedirect('#')   #path of deleteforbbiddenWord.html


def addcomment(request,postid):
	if request.method=='POST':
		post_get = get_object_or_404(Post,pk = postid)
		user_get = request.user
		con = request.POST.get('comment')
		obj = Comments(comment_text = con , post = post_get , user = user_get)
		obj.save()
		return HttpResponseRedirect('/app/showpost/'+str(postid))





