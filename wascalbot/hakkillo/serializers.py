from typing import Pattern
from django.db import models
from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import Field
from hakkillo.models import intent

class intentSerializer(serializers.ModelSerializer):
    class Meta:
        model = intent
        fields = '__all__'