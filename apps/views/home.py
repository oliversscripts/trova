from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


@login_required
def HomeView(request):
    context = {}
    return render(request, 'home.default.html', context=context)


@login_required
def IndexView(request):
    return HttpResponseRedirect(reverse('HomeView'))
