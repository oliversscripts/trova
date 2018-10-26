from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


urlpatterns = [
    url(r'^$', IndexView, name='IndexView'),
    path('apps/', HomeView, name='HomeView'),
]