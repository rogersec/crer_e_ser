from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.odonto_form, name='odonto_form'),
]