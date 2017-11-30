from django.conf.urls import url
from . import views
from fest9000.views import *

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
]
