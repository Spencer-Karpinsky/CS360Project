from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.get_username()

    def get_bio(self):
        return self.bio

    def get_first_name(self):
        return self.user.get_full_name()

    def get_profile_pic(self):
        return self.profile_pic

class Post(models.Model):
    caption = models.TextField(max_length=4000)
    title = models.TextField(max_length=50)
    created_by = models.ForeignKey(User, null=False,)
    created_at = models.DateTimeField(auto_now_add=True)
    net_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + "- Created By: " + self.created_by

    def get_title(self):
        return self.title

    def get_caption(self):
        return self.caption

    def get_net_likes(self):
        return self.net_likes

    def get_creator(self):
        return self.created_by

class Post_shared_with(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    shared_id = models.ForeignKey(User, on_delete=models.CASCADE)
