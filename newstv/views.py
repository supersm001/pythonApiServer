from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from newstv.models import Channel
from newstv.serializers import ChannelSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is Home Page")


class ChannelViewSet(viewsets.ModelViewSet):
    queryset= Channel.objects.all()
    serializer_class= ChannelSerializer
