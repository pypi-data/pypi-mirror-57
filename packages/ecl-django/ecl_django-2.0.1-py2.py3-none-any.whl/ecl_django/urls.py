from django.conf.urls.defaults import patterns
from .utils import simple_url, template_url

urlpatterns = patterns('ecl_django.views',
    simple_url('auth/password/reset'),
    simple_url('auth/password/reset/request'),
    template_url('auth/password/reset/sent'),
)

