from django.db.models import Q
from rest_framework.generics import (
  ListAPIView, CreateAPIView,
  RetrieveUpdateAPIView,
  RetrieveAPIView,
  DestroyAPIView
)
from rest_framework import pagination
from rest_framework.permissions import (
 IsAuthenticatedOrReadOnly
)
from ...core.pagination import PostLimitOffsetPagination
from ...core.common import IsAdminUser, IsUser, IsOwnerOrReadOnly

from .serializers import TABLE, LoanSerializer, LoanCreateSerializer, LoanRequestStatusSerializer, LoanStatusSerializer
from rest_framework import permissions

class LoanListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = TABLE.objects.all()

        page_size_key = 'page_size'
        page_size = self.request.GET.get(page_size_key)
        query = self.request.GET.get('q')
        pagination.PageNumberPagination.page_size = page_size if page_size else 10

        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        return queryset_list.order_by('-id')

# return members own requests
class LoanRequestAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = LoanSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = TABLE.objects.filter(user_id=self.request.user.id)

        page_size_key = 'page_size'
        page_size = self.request.GET.get(page_size_key)
        query = self.request.GET.get('q')
        pagination.PageNumberPagination.page_size = page_size if page_size else 10

        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        return queryset_list.order_by('-id')


class LoanCreateAPIView(CreateAPIView):
    serializer_class = LoanCreateSerializer
    permission_classes = [IsUser]
    queryset = TABLE.objects.all()
    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)

class LoanDetailAPIView(RetrieveAPIView):
    queryset = TABLE.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LoanSerializer

class LoanDeleteAPIView(DestroyAPIView):
    queryset = TABLE.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = LoanSerializer

class LoanUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TABLE.objects.all()
    serializer_class = LoanSerializer

# for updating request status to either accepted or rejected
class LoanRequestStatusUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = TABLE.objects.all()
    serializer_class = LoanRequestStatusSerializer

# for updating loan status to either taken or returned
class LoanStatusUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = TABLE.objects.all()
    serializer_class = LoanStatusSerializer
