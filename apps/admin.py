from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


# Config
admin.site.register(ConfigWebServiceModel)

# Users & Profiles
admin.site.register(UserModel)
admin.site.register(UserProfileModel)

# TV Data
admin.site.register(TvShowModel)