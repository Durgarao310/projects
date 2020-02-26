from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    LAN          = [('py','python'),('js','javascript'),('ja','java'),('.net','dotnet'),('php','php')]
    author       = models.ForeignKey(User, on_delete=models.CASCADE)
    title        = models.CharField(max_length=200)
    date_posted  = models.DateTimeField(default=timezone.now)
    code         = models.TextField()
    pro_language = models.CharField(choices=LAN, max_length=4, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
    @property
    def likes(self):
        return PostLike.objects.filter(post=self).count()

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.title} by {self.user.username}'

class Comment(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post    = models.ForeignKey('main.post', on_delete=models.CASCADE)
    text = models.TextField()
    date    = models.DateTimeField(auto_now=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment
    

  