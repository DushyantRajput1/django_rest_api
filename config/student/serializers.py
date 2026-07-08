from rest_framework import serializers

from users.models import User
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Student
        fields = [
            "student_id",
            "user",
            "university",
            "college",
            "degree",
            "specialization",
            "current_year",
            "expected_year_of_passing",
            "cgpa",
            "percentage",
            "date_of_birth",
            "gender",
            "permanent_address",
            "current_address",
            "interested_domain",
            "preferred_job_role",
            "career_goal",
            "is_profile_completed",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["student_id", "created_at", "updated_at"]

    def to_internal_value(self, data):
        if isinstance(data, dict) and "user" in data and isinstance(data["user"], str):
            try:
                student = Student.objects.get(student_id=data["user"])
                data = data.copy()
                data["user"] = student.user_id
            except Student.DoesNotExist:
                pass
        return super().to_internal_value(data)

    def validate(self, attrs):
        if self.instance is None and "user" not in attrs:
            raise serializers.ValidationError({"user": "This field is required."})
        return attrs