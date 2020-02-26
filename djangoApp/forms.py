from django import forms
from .models import Posts,Users

class PostForm(forms.ModelForm):
	class Meta:
		model = Posts
		fields = ('post_title','post_text','post_date','post_image','user_id','cat')

class UserForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ('user_name','user_email','user_pass')