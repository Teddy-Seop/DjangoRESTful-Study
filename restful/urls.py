from django.conf.urls import url,include
from . import views

urlpatterns = [
    url('list/$', views.postsList.as_view(), name='postsList'),
    url('list/(?P<id>\d+)/$', views.postsDetail.as_view(), name='postsDetail'),
]