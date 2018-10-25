from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('apps.urls')),
]
