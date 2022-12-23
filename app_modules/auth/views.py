from app_modules.auth.serializers import CustomRegisterSerializer
from app_modules.base.viewsets import BaseCreateViewSet
from app_modules.users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class CustomRegistrationViewSet(BaseCreateViewSet):
    """
    User registration
    """

    serializer_class = CustomRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = RefreshToken.for_user(user)
        response = {
            "user" : UserSerializer(user).data,
            "access_token" : str(tokens.access_token),
            "refresh_token" : str(tokens)
        }
        return Response(response)