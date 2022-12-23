from rest_framework import serializers
from app_modules.users.models import User
from app_modules.users.serializers import UserSerializer


class CustomRegisterSerializer(serializers.ModelSerializer):
    """
    User registration serializer
    """

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["name", "username", "email", "password1", "password2"]

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("A user is already exists with this email.")
        return value

    def validate_username(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("A user is already exists with this email.")
        return value

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data.get("name"),
            username=validated_data.get("username"),
            email=validated_data.get("email"),
        )
        user.set_password(validated_data.get("password1"))
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    User Login Serializer
    """

    user = serializers.SerializerMethodField()
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    def get_user(self, obj):
        user = obj["user"]
        return UserSerializer(user).data
