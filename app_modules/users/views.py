from app_modules.base.viewsets import BaseGenericViewSet
from app_modules.users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.


class UserProfileViewSet(BaseGenericViewSet):
    """
    User Profile
    """

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    @action(detail=False, methods=["PUT"], url_path="profile/update", url_name="profile-update")
    def profile_update(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data)

    @action(detail=False, methods=["GET"], url_path="profile", url_name="profile-retrieve")
    def profile_retrieve(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
