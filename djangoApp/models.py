from django.db import models


# class Post(models.Model):
# 	post_id=models.AutoField(primary_key=True)
# 	title=models.CharField(max_length=200)
# 	date=models.DateTimeField()
# 	image = models.ImageField(upload_to ='Images/')
# 	content = models.TextField()
# 	user_id=models.ForeignKey(UserModel, on_delete=models.CASCADE)
# 	cat_id=models.ForeignKey(Category, on_delete=models.CASCADE)
	
# class post_likes(models.Model):
# 	post_id=models.ForeignKey(Post, on_delete=models.CASCADE)
# 	user_id=models.ForeignKey(UserModel, on_delete=models.CASCADE)
# 	like=models.BooleanField(default=False)

# class Tag(models.Model):
# 	tag_id=models.AutoField(primary_key=True)
# 	name=models.CharField(max_length=200)
# 	post_id=models.ForeignKey(Post, on_delete=models.CASCADE)
# 	cat_id=models.ForeignKey(Category, on_delete=models.CASCADE)

# class Forbidden_Words(models.Model):
# 	word_id=models.AutoField(primary_key=True)
# 	word=models.CharField(max_length=200)




