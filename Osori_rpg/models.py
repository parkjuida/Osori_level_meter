from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    git_commit = models.IntegerField(default=0)
    room_visit = models.IntegerField(default=0)
    event_visit = models.IntegerField(default=0)
    contribution = models.IntegerField(default=0)
    login_counter = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
