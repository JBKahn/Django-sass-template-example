from rest_framework import serializers

from home.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ( 'item', 'is_done', 'id' )