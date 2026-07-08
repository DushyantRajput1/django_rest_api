from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializers import StudentSerializer
from .services import StudentService


class StudentListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        students = StudentService.get_all_students()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        student = StudentService.create_student(serializer.validated_data)
        response_serializer = StudentSerializer(student)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        user_value = request.data.get("user")
        student_instance = StudentService.get_student_by_user_or_id(user_value)

        if student_instance is None:
            return Response(
                {"detail": "Student not found for the provided user or student id."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = StudentSerializer(student_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        student = StudentService.update_student(student_instance, serializer.validated_data)
        response_serializer = StudentSerializer(student)
        return Response(response_serializer.data, status=status.HTTP_200_OK)


class StudentDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        student = StudentService.get_student_by_id(pk)
        if student is None:
            return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        student_instance = StudentService.get_student_by_id(pk)
        if student_instance is None:
            return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        student = StudentService.update_student(student_instance, serializer.validated_data)
        response_serializer = StudentSerializer(student)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        student = StudentService.get_student_by_id(pk)
        if student is None:
            return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
