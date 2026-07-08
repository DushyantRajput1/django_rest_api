from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from student.models import Student
from users.models import User


class StudentAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="student@example.com",
            password="password123",
            first_name="John",
            last_name="Doe",
            phone_number="1234567890",
        )

    def test_create_and_list_students(self):
        url = reverse("student-list-create")
        payload = {
            "user": self.user.pk,
            "career_goal": "Become a backend engineer",
            "cgpa": "3.80",
        }

        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_update_and_delete_student(self):
        student = Student.objects.create(user=self.user)
        url = reverse("student-detail", kwargs={"pk": student.student_id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        update_payload = {
            "career_goal": "Become a full-stack engineer",
            "cgpa": "3.90",
        }
        response = self.client.put(url, update_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["career_goal"], "Become a full-stack engineer")

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(student_id=student.student_id).exists())

    def test_put_updates_existing_student_using_student_uuid(self):
        student = Student.objects.create(user=self.user)
        url = reverse("student-list-create")
        payload = {
            "user": str(student.student_id),
            "career_goal": "Backend Developer",
            "cgpa": "3.80",
        }

        response = self.client.put(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        student.refresh_from_db()
        self.assertEqual(student.career_goal, "Backend Developer")
