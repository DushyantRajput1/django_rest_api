from .models import User ,OTPVerification
from .utils import send_otp_email , generate_otp
from django.utils import timezone
from datetime import timedelta
from django.db import transaction

class UserService:

    @staticmethod
    @transaction.atomic
    def signup(validated_data):
        otp = generate_otp()

        validated_data.pop("confirm_password")
        password = validated_data.pop("password")

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        OTPVerification.objects.create(
            user=user,
            otp=otp,
            expires_at=timezone.now() + timedelta(minutes=5)
        )

        send_otp_email(user.email, otp)

        return user
    

class OTPVerificationService:
    
    @staticmethod
    @transaction.atomic
    def verify_otp(email, otp):
        try:
            user = User.objects.get(email=email)
            otp_verification = OTPVerification.objects.get(user=user, otp=otp)

            if otp_verification.expires_at < timezone.now():
                return False, "OTP has expired."

            user.is_verified = True
            user.save()

            otp_verification.delete()

            return True, "OTP verified successfully."
        except User.DoesNotExist:
            return False, "User does not exist."
        except OTPVerification.DoesNotExist:
            return False, "Invalid OTP."
        


class LOGINService:
    @staticmethod
    @transaction.atomic
    def login(email, password):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                user.last_login = timezone.now()
                user.save(update_fields=["last_login"])

                return True, "Login successful."
            else:
                return False, "Invalid password."
        except User.DoesNotExist:
            return False, "User does not exist."
        


class UserServicelist:
    @staticmethod
    def get_all_users(user_id=None):

        users = User.objects.filter(
            is_verified=True,
            is_active=True
        )

        return users
    

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = User.objects.get(
    id=user_id,
    is_verified=True,
    is_active=True
)
            return user
        except User.DoesNotExist:
            return None