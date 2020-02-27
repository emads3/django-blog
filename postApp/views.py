from django.http import Http404
from django.shortcuts import render

# Create your views here.
from postApp.models import Posts, Comments, Post_Likes_Dislikes


def single_post(request, num):
	try:
		post = Posts.objects.get(id=num)
	except Posts.DoesNotExist:
		raise Http404("Post Not Found")

	# get bad words in array
	# loop on post on every word.. check if this word in array of bad words

	comment = Comments.objects.filter(post_id=num)
	likes_dislikes = Post_Likes_Dislikes.objects.filter(post=num)
	context = {'post': post, 'comments': comment, 'likes_dislikes': likes_dislikes}
	return render(request, 'post_page.html', context)


'''
try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question doesn't exist")
	return render(request, 'polls/detail.html', {'question': question, })
'''
