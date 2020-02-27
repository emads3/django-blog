from django import forms
from djangoApp.models import  Post ,  Categories , Tag
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['post_title','post_image','post_text','post_date','cat','user_id']

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Categories
		fields = ['cat_name'] #hna hzwod el fields bta3t el category elly h3adl 3leha

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['name' ,'post_tag'] #hna hzwod el fields bta3t el category elly h3adl 3leha

class UserForm(forms.ModelForm):
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = ('id','username', 'password' , 'email','is_active' , 'is_staff' , 'is_superuser') #hna hzwod el fields bta3t el users elly h3adl 3leha

	def clean_password2(self):
		cleaned_data=super(UserForm , self).clean()
		password=cleaned_data.get('password')
		password2=cleaned_data.get('password2')

		if password and password2 and password != password2:
			raise forms.ValidationError('passwords do not match')
		return password2