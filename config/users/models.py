# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class User(AbstractUser):
#     phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

#     ROLE_CHOICES = (
#         ("ADMIN", "Admin"),
#         ("USER", "User"),
#     )

#     role = models.CharField(
#         max_length=20,
#         choices=ROLE_CHOICES,
#         default="USER"
#     )

#     is_verified = models.BooleanField(default=False)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.username


from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager

from datetime import datetime
from django.utils import timezone
import uuid

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)

    phone_number = models.CharField(
        max_length=15,
        unique=True
    )

    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("USER", "User"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="USER",
    )

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone_number",
    ]

    objects = UserManager()

    def __str__(self):
        return self.email
    


class OTPVerification(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="otps"
    )

    otp = models.CharField(max_length=6)

    expires_at = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "otp_verification"

    def __str__(self):
        return f"{self.user.email} - {self.otp}"