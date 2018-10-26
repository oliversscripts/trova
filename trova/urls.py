from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *

from django.contrib.auth import views

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='auth.login.html',)),
    path('logout/', views.LogoutView.as_view(template_name='auth.logout.html',)),
    path('admin/', admin.site.urls),
    url(r'^', include('apps.urls')),
]