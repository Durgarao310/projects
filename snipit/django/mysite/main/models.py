from django.db import models
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    LAN          = [('python','python'),('javascript','javascript'),('java','java'),('.net','dotnet'),('php','php')]
    title        = models.CharField(max_length=200)
    code         = models.TextField()
    date_posted  = models.DateTimeField(default=timezone.now)
    author       = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    pro_lang     = models.CharField(choices=LAN, max_length=20, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


    @property
    def likes(self):
        return PostLike.objects.filter(post=self).count()

# @login_required
class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.post.title} by {self.user.username}'

class Comment(models.Model): 
    author = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    post = models.ForeignKey('main.post', on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(default=timezone.now)
    comment = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



