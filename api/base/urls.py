from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views

urlpatterns = [

    url(r'^photo/$', views.photoListAPIView.as_view(), name='photo-list'),
    url(r'^category/$', views.categoryListAPIView.as_view(), name='category-list'),
    url(r'^check/$', views.CkeckVersionAPIView.as_view(), name='ckeck-version'),
    url(r'^bkey/$', views.KeyAPIView.as_view(), name='ckeck-version'),
    url(r'^coin/$', views.CkeckCoinAPIView.as_view(), name='ckeck-coin'),
    url(r'^cash/$', views.CashCoinAPIView.as_view(), name='cash-coin'),
    url(r'^crphoto/$', views.PhotoAPIView, name='create_photo'),

    url(r'^user/create/$', views.CreateUserAPIView, name='create_user'),
    url(r'^tokencreate/', obtain_jwt_token),
    url(r'^token/refresh/', refresh_jwt_token),
    url(r'^token/verify/', verify_jwt_token),

]
