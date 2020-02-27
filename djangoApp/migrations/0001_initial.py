# Generated by Django 3.0.3 on 2020-02-27 12:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_image', models.ImageField(upload_to='Posts/')),
                ('post_text', models.CharField(max_length=900, null=True)),
                ('post_date', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 12, 44, 30, 562329, tzinfo=utc))),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Categories')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('post_tag', models.ManyToManyField(to='djangoApp.Post')),
            ],
        ),
        migrations.CreateModel(
            name='post_likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=400)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 12, 44, 30, 563043, tzinfo=utc))),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='djangoApp.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
