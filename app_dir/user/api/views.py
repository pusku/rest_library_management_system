from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView,
    RetrieveAPIView, DestroyAPIView
)

from django.db.models import Q
from rest_framework import pagination
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticatedOrReadOnly, IsAuthenticated)
from .serializers import UserSerializer, User, ProfileSerializer, UserProfile, MemberRegistrationSerializer
from ...core.pagination import PostLimitOffsetPagination
from ...core.common import IsAdminUser, IsUser, IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser, FileUploadParser
from django.http import HttpResponse

class UserListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()

        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(username__icontains=query)
            )

        return queryset_list.order_by('-id')


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()


class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser)

class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer


class UpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class ProfileView(RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

class MemberRegistrationAPIView(CreateAPIView):
    serializer_class = MemberRegistrationSerializer
    permission_classes = [IsUser]
    queryset = User.objects.all()

class MemberProfileUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = MemberRegistrationSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)