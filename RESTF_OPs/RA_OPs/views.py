from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import request, serializers
from rest_framework.parsers import JSONParser
from RA_OPs.models import *
from RA_OPs.serializers import *
from rest_framework import viewsets


class CrudpViewsets(viewsets.ModelViewSet):
    queryset=Crudp.objects.all()
    serializer_class=Crudpserializers

class jobViewsets(viewsets.ModelViewSet):
    queryset=job.objects.all()
    serializer_class=jobserializers

class addressViewsets(viewsets.ModelViewSet):
    queryset=address.objects.all()
    serializer_class=addressserializers
