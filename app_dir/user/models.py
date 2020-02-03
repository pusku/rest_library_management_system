from django.db import models
from django.contrib.auth import get_user_model

class UserProfile(models.Model):
    User = get_user_model()
    user   = models.OneToOneField(User,on_delete=models.CASCADE,)
    image = models.ImageField(upload_to="accounts/images/", null=True, blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=False,
        null=True)