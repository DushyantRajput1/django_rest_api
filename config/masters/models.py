from django.db import models

from datetime import datetime
from django.utils import timezone
import uuid


class University(models.Model):
    university_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    short_name = models.CharField(
        max_length=100,
        unique=True
    )
    website = models.URLField(
        max_length=255,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=100
    )
    state = models.CharField(
        max_length=100
    )
    cuntry = models.CharField(
        max_length=100
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    upated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "university"

    def __str__(self):
        return self.name
    


class  College(models.Model):
    collage_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name="collages"
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    short_name = models.CharField(
        max_length=100,
        unique=True
    )
    code = models.CharField(
        max_length=50,
        unique=True
    )

    website = models.URLField(
        max_length=255,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=100
    )
    state = models.CharField(
        max_length=100
    )
    cuntry = models.CharField(
        max_length=100
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    upated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "collage"

    def __str__(self):
        return self.name
    


class Degree(models.Model):
    degree_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE,
        related_name="degrees"
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    short_name = models.CharField(
        max_length=100,
        unique=True
    )
    code = models.CharField(
        max_length=50,
        unique=True
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    upated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "degree"

    def __str__(self):
        return self.name
    

class Specialization(models.Model):
    specialization_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    degree = models.ForeignKey(
        Degree,
        on_delete=models.CASCADE,
        related_name="specializations"
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    short_name = models.CharField(
        max_length=100,
        unique=True
    )
    code = models.CharField(
        max_length=50,
        unique=True
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    upated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "specialization"

    def __str__(self):
        return self.name
    

class Skill(models.Model):
    skill_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    short_name = models.CharField(
        max_length=100,
        unique=True
    )
    code = models.CharField(
        max_length=50,
        unique=True
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    upated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "skills"

    def __str__(self):
        return self.name