from django import forms
from djangoApp.models import Forbidden_Words #  Post ,Categories # ,User , 

# class UserForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ( 'id','username','email','is_active')  #hna hzwod el fields bta3t el users elly h3adl 3leha

# class PostForm(forms.ModelForm):
# 	class Meta:
# 		model = Post
		# fields = (****) #hna hzwod el fields bta3t el posts elly h3adl 3leha

# class CategoryForm(forms.ModelForm):
# 	class Meta:
# 		model = Categories
		# fields = (****) #hna hzwod el fields bta3t el category elly h3adl 3leha

class ForbiddenForm(forms.ModelForm):
	class Meta:
		model = Forbidden_Words
		fields = ('word_id' , 'word') #hna hzwod el fields bta3t el forbidden word elly h3adl 3leha