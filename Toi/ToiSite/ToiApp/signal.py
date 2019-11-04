from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs): # creating a new profile for when a user registers
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kwargs): # creating a new profile for when a user registers
    instance.profile.save()
