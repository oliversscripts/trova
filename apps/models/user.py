from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


class User(AbstractUser):
    plex_id = models.CharField(blank=True, max_length=254)
    user_profile = models.ForeignKey('apps.UserProfile', blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % (self.username)


class UserProfile(models.Model):
    name = models.CharField(blank=False, max_length=254)
    manager = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    
    def __str__(self):
        return '%s' % (self.name)

    def is_admin(self):
        return self.admin
    
    def is_manager(self):
        return self.manager