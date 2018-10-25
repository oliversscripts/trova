from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


def Index(request):
    return HttpResponseRedirect(reverse('home'))


def Home(request):
    context = {}
    return render(request, 'home.default.html', context=context)