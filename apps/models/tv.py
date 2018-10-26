from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


class TvShowModel(models.Model):
    tvdb_id = models.IntegerField('TVDB Id', primary_key=True)
    sonarr_id = models.IntegerField('Sonarr Id', unique=True)

    title = models.CharField('Title', blank=False, max_length=254)
    slug = models.CharField('Title Slug', blank=False, max_length=254)
    overview = models.TextField('Overview', blank=True)

    image_url_banner = models.URLField('Banner Image URL', blank=True, max_length=254)
    image_url_poster = models.URLField('Poster Image URL', blank=True, max_length=254)
    image_url_fanart = models.URLField('Fan Art Image URL', blank=True, max_length=254)