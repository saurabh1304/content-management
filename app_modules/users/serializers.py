from rest_framework import serializers
from app_modules.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """

    class Meta:
        model = User
        fields = ["id", "username", "email", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
