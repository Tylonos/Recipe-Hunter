
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    



class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='profile_pics/', blank=True,null=True)

    def __str__(self):
        return f"{self.user.username} Profile"


@receiver(post_save, sender= User)
def create_or_update_user_profile(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create( user=instance )
    else:
        instance.profile.save()