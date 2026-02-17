from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    """
    Extended user profile model with additional fields
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    company = models.CharField(max_length=500, blank=True)
    designation = models.CharField(max_length=500, blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=200, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        """Override save to resize profile pictures"""
        super().save(*args, **kwargs)
        
        # if self.profile_picture:
        #     img = Image.open(self.profile_picture.path)
            
        #     # Resize if image is too large
        #     if img.height > 300 or img.width > 300:
        #         output_size = (300, 300)
        #         img.thumbnail(output_size)
        #         img.save(self.profile_picture.path)


# Signal to automatically create profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
