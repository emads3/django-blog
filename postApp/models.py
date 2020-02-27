from django.db import models

from django.utils import timezone


class Users(models.Model):
	user_name = models.CharField(max_length=100)
	user_email = models.CharField(max_length=100)
	user_pass = models.CharField(max_length=100)

	def __str__(self):
		return self.user_name


class Categories(models.Model):
	cat_name = models.CharField(max_length=100)

	def __str__(self):
		return self.cat_name


class Posts(models.Model):
	post_title = models.CharField(max_length=100)
	post_image = models.ImageField(default='default.png', null=True)
	post_text = models.CharField(max_length=900, null=True)
	post_date = models.DateTimeField(default=timezone.now())
	user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
	cat = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.post_text


class Comments(models.Model):
	comment_text = models.CharField(max_length=400)
	date = models.DateTimeField(default=timezone.now())
	post_id = models.ForeignKey(Posts, on_delete=models.DO_NOTHING)
	user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.comment_text


class Tags(models.Model):
	tag_name = models.CharField(max_length=100)
	post_id = models.ForeignKey(Posts, on_delete=models.DO_NOTHING)
	cat = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)


class Post_Tags(models.Model):
	post_id = models.ForeignKey(Posts, on_delete=models.DO_NOTHING)
	tag_id = models.ForeignKey(Tags, on_delete=models.DO_NOTHING)


class Forbidden_Words(models.Model):
	forbidden_word = models.CharField(max_length=100)


class PostRate(models.Model):
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	post = models.ForeignKey(Posts, on_delete=models.CASCADE)
	rate = models.IntegerField

class Post_Likes_Dislikes(models.Model):
	post = models.ForeignKey(Posts, on_delete=models.DO_NOTHING)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
