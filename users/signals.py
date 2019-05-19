from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import reciever
from .models import profile

@reciever(post_save, sender=User)
def create_profile(sender, inatance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@reciever(post_save, sender=User)
def save_profile(sender, inatance, **kwargs):
    instance.profile.save()
