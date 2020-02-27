from django.urls import path

from djangoApp import views
from postApp import views as postAppViews

urlpatterns = [
	path('viewpost/<num>/', postAppViews.single_post, name='viewpost'),
]
