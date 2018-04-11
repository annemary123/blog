from django.urls import path
from . import views

urlpatterns=[
path('',views.index),
path('register/',views.regist),
path('login/',views.login),
path('login/rp/',views.rstpwd),
path('login/blog/',views.cblog),
path('logout/',views.logout)
]
