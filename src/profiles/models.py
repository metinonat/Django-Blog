from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

cities = (('54', 'Sakarya'),
            ('6', 'Ankara'),
            ('7', 'Antalya'))


class Profile(models.Model):
    user = models.OneToOneField(to='auth.User', on_delete=models.CASCADE)
    picture = models.ImageField(blank=True)
    city = models.CharField(choices=cities, max_length = 20)

    def __str__(self):
        return f"{self.user.username} "

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
