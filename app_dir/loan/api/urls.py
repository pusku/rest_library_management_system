from django.urls import path
from .views import (
   LoanCreateAPIView,
   LoanListAPIView,
   LoanDeleteAPIView,
   LoanDetailAPIView,
   LoanUpdateAPIView,
   LoanRequestStatusUpdateAPIView,
   LoanStatusUpdateAPIView,
   LoanRequestAPIView
)

urlpatterns = [
    path('', LoanListAPIView.as_view(), name='list'),
    path('create', LoanCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', LoanDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', LoanDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', LoanUpdateAPIView.as_view(), name='update'),
    path('request_status/update/<int:pk>/', LoanRequestStatusUpdateAPIView.as_view(), name='request-update'),
    path('status/update/<int:pk>/', LoanStatusUpdateAPIView.as_view(), name='status-update'),
    path('request', LoanRequestAPIView.as_view(), name='request')
]
