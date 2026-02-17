from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response



class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "message" : "User Created successfully",
            "token" : token.key,
            "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "bio": user.bio,
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message" : "Login Success",
                "token" : token.key
            })
        else:
            return Response(serializer.errors, status=400)


