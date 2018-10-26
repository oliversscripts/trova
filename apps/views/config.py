from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *

@login_required
def ConfigWebServiceView(request):
    context = {}
    
    # if request.method == 'POST':
    #     web_services_config_data = WebServicesConfig.objects.all()[0]
    #     web_services_config_form = WebServicesConfigForm(request.POST, instance=web_services_config_data)
        
    #     if web_services_config_form.is_valid():
    #         web_services_config_form.save()
    #         messages.success(request, 'Web Services Config Saved')
    #     else:
    #         messages.error(request, 'Problem saving Web Services Config')
        
    # else:
    #     if WebServicesConfig.objects.all().exists():
    #         web_services_config_data = WebServicesConfig.objects.all()[0]
    #         web_services_config_form = WebServicesConfigForm(instance=web_services_config_data)
    #     else:
    #         web_services_config_data = WebServicesConfig()
    #         web_services_config_data.save()
    #         web_services_config_form = WebServicesConfigForm(instance=web_services_config_data)

    # reponse_data['form'] = web_services_config_form

    return render(request, '', context=context)