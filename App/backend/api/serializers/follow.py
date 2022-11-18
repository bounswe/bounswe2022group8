from rest_framework import serializers
from ..models.user import Follow


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["id", "from_user", "to_user", "created_at"] 

