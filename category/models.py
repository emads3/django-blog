from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=200)
    cat_user = models.ManyToManyField(User)