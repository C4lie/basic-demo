from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Login: Obtain token for authenticated users
class UserLoginView(TokenObtainPairView):
    pass

# Token refresh: Allow users to get a new token
class TokenRefreshView(TokenRefreshView):
    pass

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
