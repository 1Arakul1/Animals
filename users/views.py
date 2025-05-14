from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .permissions import IsSuperUser, IsSelf
from rest_framework.exceptions import PermissionDenied
import logging

logger = logging.getLogger(__name__)

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]

    def get(self, request, *args, **kwargs):
        logger.debug(f"Authorization header: {request.META.get('HTTP_AUTHORIZATION')}")
        return super().get(request, *args, **kwargs)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsSelf]

    def get_object(self):
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        if not self.request.user == user and not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to access this user's profile.")
        return user