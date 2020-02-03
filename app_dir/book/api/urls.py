from django.urls import path
from .views import (
   BookCreateAPIView,
   BookListAPIView,
   BookDeleteAPIView,
   BookDetailAPIView,
   BookUpdateAPIView,
   BookListByAuthorAPIView,
   ExcelExportView
)

urlpatterns = [
    path('', BookListAPIView.as_view(), name='list'),
    path('create', BookCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', BookDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', BookDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', BookUpdateAPIView.as_view(), name='update'),
    path('filter/author/<int:pk>/', BookListByAuthorAPIView.as_view(), name='filter-author'),
    path('export/excel', ExcelExportView.as_view(), name='export-excel')
]
