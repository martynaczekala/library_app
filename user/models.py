from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

logger=logging.getLogger('django')

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    
    """def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        try:
            p=Permission.objects.get(codename='can_rent')
            self.user_permissions.add(p)
        except Exception as e:
            logger.log(logging.ERROR, "%s" % e)"""
        
        
    #signals
@receiver(post_save, sender=User)
def add_rent_permission(sender, *args, **kwargs):
    user = kwargs.get('instance')
    try:
        p=Permission.objects.get(codename='can_rent')
        user.user_permissions.add(p)
        logger.info("Permissions added")
    except Exception as e:
        logger.error("Error:Permission not added: %s" % e)