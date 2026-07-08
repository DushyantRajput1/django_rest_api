from django.test import TestCase

from .serializers import SignUpSerializer


class SignUpSerializerTests(TestCase):
    def test_accepts_student_role_with_lowercase_value(self):
        data = {
            "email": "student@example.com",
            "phone_number": "+919999999999",
            "password": "Password123",
            "confirm_password": "Password123",
            "role": "student",
            "first_name": "Test",
            "last_name": "User",
        }

        serializer = SignUpSerializer(data=data)

        self.assertTrue(serializer.is_valid(), serializer.errors)
        self.assertEqual(serializer.validated_data["role"], "STUDENT")
