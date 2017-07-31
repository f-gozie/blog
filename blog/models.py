from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from tinymce import models as tinymce_models
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',null=True)
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now())
    text = models.TextField()
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    email = models.EmailField(max_length=50, default='kingdom@gmail.com')

    def save(self, *args, **kwargs):
        # self.author = self.author.upper()
        self.slug = slugify(self.title)
        super(Post, self).save(*args,**kwargs)
    def publish(self):
        self.pub_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.ForeignKey('auth.User')
    email = models.EmailField(max_length=50)
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(default=timezone.now())
    text = tinymce_models.HTMLField()

    def __str__(self):
        return self.text
