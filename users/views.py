from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """Контроллер для представления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return self.queryset.all()


class UserCreateAPIView(CreateAPIView):
    """Контроллер для создания пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)


class MyTokenObtainPairView(TokenObtainPairView):
    pass  # Использует стандартный функционал


class MyTokenRefreshView(TokenRefreshView):
    pass  # Использует стандартный функционал
