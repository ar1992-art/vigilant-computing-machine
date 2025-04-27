from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, UserSerializer
from portfolio.models import Portfolio


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        # 1) create the user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # 2) **create their Portfolio**
        Portfolio.objects.create(user=user)

        # 3) generate tokens
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        # 4) return profile + tokens
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'access': access,
            'refresh': str(refresh),
        })


class UserMeView(generics.RetrieveAPIView):
    """
    GET /api/auth/me/
    Returns the current authenticated user's profile.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
