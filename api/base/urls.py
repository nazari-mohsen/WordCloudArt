from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views
from django.urls import re_path
urlpatterns = [

    re_path(r'^photo/$', views.photoListAPIView.as_view(), name='photo-list'),
    re_path(r'^devphotolab/$', views.photoListDevelopAPIView.as_view(), name='photo-develop'),
    re_path(r'^category/$', views.categoryListAPIView.as_view(), name='category-list'),
    re_path(r'^devcategorylab/$', views.categoryListDevelopAPIView.as_view(), name='category-Develop'),
    re_path(r'^check/$', views.CkeckVersionAPIView.as_view(), name='ckeck-version'),
    re_path(r'^help/$', views.HelpListAPIView.as_view(), name='help'),
    re_path(r'^bkey/$', views.KeyAPIView.as_view(), name='ckeck-version'),
    re_path(r'^coin/$', views.CkeckCoinAPIView.as_view(), name='ckeck-coin'),
    re_path(r'^cash/$', views.CashCoinAPIView.as_view(), name='cash-coin'),
    re_path(r'^crash/$', views.CrashAPIView.as_view(), name='crash'),
    re_path(r'^crphoto/$', views.PhotoAPIView, name='create_photo'),

    re_path(r'^user/create/$', views.CreateUserAPIView, name='create_user'),
    re_path(r'^tokencreate/', obtain_jwt_token),
    re_path(r'^token/refresh/', refresh_jwt_token),
    re_path(r'^token/verify/', verify_jwt_token),

]
