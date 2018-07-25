from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^add/$', views.add_device, name='add_device'),
    url(r'^all/$', views.view_devices, name='view_devices'),

]

