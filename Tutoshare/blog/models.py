from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
User = settings.AUTH_USER_MODEL

class Technology(models.Model):
    title = models.CharField(max_length=150)
    img = models.URLField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.title

type_choices = (
    ("BOOK", "BOOK"),
    ("VIDEO", "VIDEO"),
)

plan_choices = (
    ("FREE", "FREE"),
    ("PAID", "PAID"),
)
audience_choices = (
    ("BEGINNER", "BEGINNER"),
    ("ADVANCED", "ADVANCED"),
)

class Tutorial(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    url = models.URLField(max_length=150)
    websitename = models.CharField(max_length=150)
    tech = models.ForeignKey('Technology',on_delete=models.CASCADE)
    type = models.CharField(max_length=150, choices=type_choices, default="VIDEO")
    plan = models.CharField(max_length=150, choices=plan_choices, default="FREE")
    audience = models.CharField(max_length=150, choices=audience_choices, default="BEGINNER")
    upvote = models.IntegerField(default=0)

    @property
    def is_user_upvoted(self, user):
        upvote = Upvote.objects.filter(tutorial=self, user=user).first()
        return bool(upvote)

    def __str__(self):
        return "Tutorial: {}".format(self.url)

class Upvote(models.Model):
    tutorial = models.ForeignKey('Tutorial', on_delete=models.CASCADE, related_name="upvotes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)        

    def __str__(self):
        return self.tutorial
