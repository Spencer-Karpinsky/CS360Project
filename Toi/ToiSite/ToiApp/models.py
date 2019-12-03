from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.urls import reverse
from PIL import Image

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    friends = models.ManyToManyField(User, related_name='friends', null=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(null=True, upload_to='profile_pics', default='../media/img/ToiColors.JPG')

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_bio(self):
        return self.bio

    def get_first_name(self):
        return self.user.get_full_name()

    def get_profile_pic(self):
        return self.profile_pic

    def save(self, **kwargs):#resize images for profile pictures
        super().save()
        pic = Image.open(self.profile_pic.path)
        output_size = (250,250)
        pic.thumbnail(output_size)
        pic.save(self.profile_pic.path)


class Post(models.Model):
    photo = models.ImageField(upload_to='media/')
    caption = models.TextField(max_length=4000)
    title = models.TextField(max_length=50)
    created_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    net_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + "- Created By: " + self.created_by.username

    def get_title(self):
        return self.title

    def get_caption(self):
        return self.caption

    def get_net_likes(self):
        return self.net_likes

    def get_creator(self):
        return self.created_by

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Post_shared_with(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    shared_id = models.ForeignKey(User, on_delete=models.CASCADE)
