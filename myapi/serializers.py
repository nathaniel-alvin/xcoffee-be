from rest_framework import serializers

from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('menu_id', 'name', 'price')