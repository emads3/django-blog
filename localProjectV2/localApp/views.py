from django.shortcuts import render
from localApp.models import Users,Posts,Comments,Tags,Forbidden_Words
from django.http import HttpResponse,HttpResponseRedirect
from localApp.forms import PostForm

def home(request):
	latest_post_list = Posts.objects.all()
	context = {'latest_post_list' : latest_post_list}
	return render(request,'localApp/home.html',context)

def details(request,num):
	try:
		post = Posts.objects.get(id = num)
	except Posts.DoesNotExist:
		raise Http404("Posts does not exist")
		return render(request,'localApp/details.html',{'post',post})


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

# def sportsCat(request):
	




