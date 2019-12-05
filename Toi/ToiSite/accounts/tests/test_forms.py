from django.test import TestCase
from django.test import Client
from .forms import SignUpForm
from django.contrib.auth.models import User

class Setup_Class(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="ToiTesting1",email="user@toi.com",
        password1="jumpman23!", password2="jumpman23!", first_name="Testing", last_name="User")

class User_Form_Test(TestCase):
    def test_UserForm_valid(self):
        form = SignUpForm(data={'username':"ToiTesting1",'email':"user@toi.com",
        'password1':"jumpman23!", 'password2':"jumpman23!", 'first_name':"Testing", 'last_name':"User"})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = SignUpForm(data={'username':"",'email':"toi.com",
        'password1':"jumpman23", 'password2':"jumpman23!", 'first_name':"Testin", 'last_name':"er"})
        self.assertTrue(form.is_valid())