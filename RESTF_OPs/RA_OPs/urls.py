from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from .views import *
from rest_framework import routers, views
from RA_OPs.views import *



router = routers.DefaultRouter()
router.register(r'Crudp',CrudpViewsets)
router.register(r'job',jobViewsets)
router.register(r'address',addressViewsets)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]