from rest_framework import serializers
from .models import User

class SignUpSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'password', 'confirm_password', 'role','first_name', 'last_name']

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )

        return attrs
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value
    
    def validate_phone_number(self, value):
        if User.objects.filter(phone_number = value).exists():
            raise serializers.ValidationError("Phone number is already in use.")
        return value
    
    def validate_first_name(self ,value):
        if not value.strip():
            raise serializers.ValidationError("First name is required.")
        return value
    def validate_last_name(self ,value):
        if not value.strip():
            raise serializers.ValidationError("Last name is required.")
        return value


class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)


class LOGINSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'role', 'is_verified', 'first_name', 'last_name']

        