from django.db import models

class Categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = name = models.CharField(max_length=200)