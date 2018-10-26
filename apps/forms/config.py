from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


class ConfigWebServiceForm(ModelForm):
    class Meta:
        model = ConfigWebServiceModel
        fields = '__all__'