from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
	class Meta:
		model = Posts
		fields = ('post_title','post_text','post_date','post_image','user_id')