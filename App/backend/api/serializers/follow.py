from rest_framework import serializers
from ..models.user import Follow


class FollowSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%m', input_formats=None)
    class Meta:
        model = Follow
        fields = ["id", "from_user", "to_user", "created_at"] 

