from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.containerList.as_view(), name='containerList'),
    url(r'^(?P<c_id>\d+)/$', views.containerDetail.as_view(), name='containerDetail'),
    url(r'^container/(?P<c_id>\d+)/update', views.containerUpdate.as_view(), name='containerUpdate'),
    url(r'^container/(?P<c_id>\d+)/delete', views.containerDelete.as_view(), name='containerDelete'),
    url(r'^container/$', views.containerCreate.as_view(), name='containerCreate'),
]