from django.urls import path

from .views import (
    UserListAPIView, UserCreateAPIView,
    UserDetailAPIView, UserDeleteAPIView,
    UpdateAPIView, ProfileView,
    MemberRegistrationAPIView, MemberProfileUpdateAPIView
)


urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('create', UserCreateAPIView.as_view(), name='user-creator'),
    path('profile/<int:pk>/', UserDetailAPIView.as_view(), name='user-profile'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-destroyer'),
    path('update/<int:pk>/', UpdateAPIView.as_view(), name='user-updater'),
    path('profile/<int:pk>/upload/', ProfileView.as_view(), name="image-upload"),
    path('registration', MemberRegistrationAPIView.as_view(), name="member-registration"),
    path('profile/update/<int:pk>/', MemberProfileUpdateAPIView.as_view(), name="profile-update")

]
