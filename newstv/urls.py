from django.contrib import admin
from django.urls import path,include
from newstv.views import ChannelViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'channels',ChannelViewSet)


urlpatterns = [
   
    path('',include(router.urls))

]
