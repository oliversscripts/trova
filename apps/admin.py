from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


# Config
admin.site.register(ConfigWebService)

# Users & Profiles
admin.site.register(User)
admin.site.register(UserProfile)

# TV Data
admin.site.register(TvShow)