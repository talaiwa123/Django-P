from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import *


class Crudpserializers(serializers.ModelSerializer):

    class Meta():
        model = Crudp
        fields = '__all__'

class jobserializers(serializers.ModelSerializer):

    class Meta():
        model = job
        fields = '__all__'

class addressserializers(serializers.ModelSerializer):

    class Meta():
        model = address
        fields = '__all__'