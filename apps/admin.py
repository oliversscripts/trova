from django.contrib import admin

from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
