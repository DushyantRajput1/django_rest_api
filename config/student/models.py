from django.db import models

from datetime import datetime
from django.utils import timezone
import uuid
from users.models import User    

class Gender(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"
    OTHER = "OTHER", "Other"


class Student(models.Model):
    student_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student"
    )

    # ===========================
    # Education Details
    # ===========================

    university = models.ForeignKey(
        "masters.University",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    college = models.ForeignKey(
        "masters.College",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    degree = models.ForeignKey(
        "masters.Degree",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    specialization = models.ForeignKey(
        "masters.Specialization",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    current_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    expected_year_of_passing = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    # ===========================
    # Personal Details
    # ===========================

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        default=Gender.OTHER
    )

    permanent_address = models.TextField(
        null=True,
        blank=True
    )

    current_address = models.TextField(
        null=True,
        blank=True
    )

    # ===========================
    # Career Details
    # ===========================

    interested_domain = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    preferred_job_role = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    career_goal = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    skills = models.ManyToManyField(
        "masters.Skill",
        blank=True,
        related_name="students"
    )

    # ===========================
    # Profile Status
    # ===========================

    is_profile_completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "student"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"