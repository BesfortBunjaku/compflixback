from .models import Component
from rest_framework import serializers

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('id', 'title', 'description', 'image', 'tag', 'code')

 
