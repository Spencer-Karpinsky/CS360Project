from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import Post, Post_shared_with, UserProfile
from .forms import PostForm

class Setup_Class(TestCase):
    def test_user1(self):
        self.user = User.objects.create(username="ToiTesting1",email="user@toi.com",
        password="jumpman23!", first_name="Testing", last_name="User")

    def test_user2(self):
        self.user = User.objects.create(username="ToiTesting2",email="user2@toi.com",
        password="jumpman23!", first_name="Testing2", last_name="User2")


class User_Post_Creation_And_Share(TestCase):
    def test_create_post(self):
        form = PostForm(data={'title': "testing", 'caption': "testing"})
        self.assertTrue(form.is_valid())

    def test_create_and_share_post(self):
        User1 = User.objects.create(username="ToiTesting1",email="user@toi.com",
        password="jumpman23!", first_name="Testing", last_name="User")
        User2 = User.objects.create(username="ToiTesting2",email="user2@toi.com",
        password="jumpman23!", first_name="Testing2", last_name="User2")
        UserPost = Post.objects.create(photo="../../media/img/ToiColors.JPG", caption="testing", title="testing", created_by=User1)
        Post_share = Post_shared_with.objects.create(post_id=UserPost, shared_id=User2)

class User_Friendship_Creation(TestCase):
    def test_create_user_and_add_friend(self):
        User1 = User.objects.create(username="ToiTesting1",email="user@toi.com",
        password="jumpman23!", first_name="Testing", last_name="User")
        User2 = User.objects.create(username="ToiTesting2",email="user2@toi.com",
        password="jumpman23!", first_name="Testing2", last_name="User2")
        User1Profile = UserProfile.objects.create(user=User1, bio="TestingBio")
        User1Profile.friends.add(User2)