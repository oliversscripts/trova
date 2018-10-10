from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


class ConfigWebServices(models.Model):
    # Trakt
    api_key_trakt_username = models.CharField('Trakt API Username', blank=True, max_length=254)
    api_key_trakt_client_id = models.CharField('Trakt API Client ID', blank=True, max_length=254)
    api_key_trakt_client_secret = models.CharField('Trakt API Client Secret', blank=True, max_length=254)

    # TVDB
    api_key_tvdb = models.CharField('TVDB API Key', blank=True, max_length=254)