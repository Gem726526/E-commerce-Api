from dataclasses import field
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
       # fields = ('__all__')(if all fields are used then using all is compulsory)
        fields =('name', 'description',) 