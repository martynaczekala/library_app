from django.db import models
#from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings

from shelf.models import BookItem
# Create your models here.

class Rental(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)
    what = models.ForeignKey(BookItem)
    when = models.DateTimeField(auto_now_add=True)
    returned=models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return "(who) rented (what)".format(who=self.who,
        what=self.what)