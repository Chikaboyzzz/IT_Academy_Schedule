from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from apps.users.serializers import UserLoginSerializer, UserCreateSerializer, LessonSerializer
from apps.users.models import User, Lesson
from rest_framework import response, status
from rest_framework.generics import get_object_or_404
from rest_framework import generics


class LessonAPIList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LoginAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.data['email'],
            password=serializer.data['password'],
        )

        if not user:
            return Response(
                data={'detail': 'Invalid Credentials or activate account'},
                status=HTTP_404_NOT_FOUND,
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            data={'token': token.key},
            status=HTTP_200_OK)


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response('user was successfully created', status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
