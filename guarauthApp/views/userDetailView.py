from django.conf import settings
from rest_framework import status, generics

from guarauthApp.models.user import User
from guarauthApp.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class UserDeleteView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)