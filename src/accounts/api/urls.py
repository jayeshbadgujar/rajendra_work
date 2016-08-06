from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
	UserList,
	UserDetail
    )

urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^$', UserList.as_view(), name='list'),
   url(r'^(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail')]
