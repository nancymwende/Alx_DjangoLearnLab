from django.shortcuts import render
from rest_framework import generics, status,permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAunthenticated
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

CustomUser = get_user_model()



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):

    user_to_follow = User.objects.get(id=user_id)

    if user_to_follow == request.user:
        return Response({"error": "You cannot follow yourself"})

    request.user.following.add(user_to_follow)

    return Response({"message": f"You are now following {user_to_follow.username}"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):

    user_to_unfollow = User.objects.get(id=user_id)

    request.user.following.remove(user_to_unfollow)

    return Response({"message": f"You unfollowed {user_to_unfollow.username}"})


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = Token.objects.get(user=user)

        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        })


class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response(
                {"error": "Invalid Credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key
        })


class ProfileView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user




class UserListView(generics.ListAPIView):
    """
    List all users
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]