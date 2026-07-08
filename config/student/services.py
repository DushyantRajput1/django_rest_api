from django.db import transaction

from .models import Student


class StudentService:
    @staticmethod
    def get_all_students():
        return Student.objects.select_related("user").all()

    @staticmethod
    def get_student_by_id(student_id):
        try:
            return Student.objects.select_related("user").get(student_id=student_id)
        except Student.DoesNotExist:
            return None

    @staticmethod
    def get_student_by_user_or_id(user_value):
        if not user_value:
            return None

        try:
            return Student.objects.select_related("user").get(student_id=user_value)
        except (Student.DoesNotExist, ValueError):
            try:
                return Student.objects.select_related("user").get(user_id=user_value)
            except (Student.DoesNotExist, ValueError):
                return None

    @staticmethod
    @transaction.atomic
    def create_student(validated_data):
        return Student.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic
    def update_student(student_instance, validated_data):
        for attr, value in validated_data.items():
            setattr(student_instance, attr, value)
        student_instance.save()
        return student_instance