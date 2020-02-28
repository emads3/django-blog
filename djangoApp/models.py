from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categories(models.Model):
	cat_name = models.CharField(max_length=200)
	cat_id = models.AutoField(primary_key=True)
	userId= models.ManyToManyField(User,blank=True)


	def __str__(self):
		return self.cat_name

class Tags(models.Model):
	name = models.CharField(max_length=200)
	# post_tag = models.ManyToManyField(Post)
	def __str__(self):
		return self.name

class Post(models.Model):
	post_title = models.CharField(max_length = 100)
	post_image = models.ImageField(upload_to='Posts/')
	post_text = models.CharField(max_length = 900 , null = True)
	post_date = models.DateTimeField(default = timezone.now())
	cat = models.ForeignKey(Categories , on_delete = models.DO_NOTHING)
	user_id = models.ForeignKey(User , on_delete = models.DO_NOTHING)
	tag = models.ManyToManyField(Tags,blank=True)

	def __str__(self):
		return self.post_title

class Comments(models.Model):
	comment_text = models.CharField(max_length = 400)
	date = models.DateTimeField(default = timezone.now())
	post = models.ForeignKey(Post , on_delete = models.DO_NOTHING)
	user = models.ForeignKey(User , on_delete = models.DO_NOTHING)
	reply = models.ForeignKey('self' , on_delete=models.CASCADE,null=True,blank=True,related_name='replies')
	
	def __str__(self):
		return self.comment_text
	
	
class post_likes(models.Model):
	post = models.ForeignKey(Post , on_delete = models.DO_NOTHING)
	user = models.ForeignKey(User , on_delete = models.DO_NOTHING)
	likes = models.IntegerField(default = 0)
	dislikes = models.IntegerField(default = 0)


class Forbidden_Words(models.Model):
	word=models.CharField(max_length=200)



class subscribe(models.Model):
	cat_id = models.name = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
	user_id = models.name = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class PostRates(models.Model):
	post_id = models.ForeignKey(Post, on_delete = models.CASCADE)
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)
	rate = models.IntegerField(null=False)

