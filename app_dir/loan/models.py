from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now
from app_dir.book.models import Book
from django.contrib.auth import get_user_model
from ..core.common import REQUEST_CHOICES, STATUS_CHOICES

class Loan(models.Model):
    User = get_user_model()

    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    book = models.ForeignKey(Book, related_name='book', on_delete=models.CASCADE)

    request = models.CharField(max_length=1, choices=REQUEST_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(
        pgettext_lazy('Loan field', 'created at'),
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        pgettext_lazy('Loan field', 'updated at'),
        default=now
    )

    class Meta:
        app_label = 'loan'

    def __str__(self):
        return self.status
