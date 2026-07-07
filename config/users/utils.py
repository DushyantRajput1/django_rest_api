import random

def generate_otp():
    return str(random.randint(100000, 999999))



from django.core.mail import send_mail
from django.conf import settings


def send_otp_email(email, otp):
    subject = "Verify your email"

    message = f"""
Hi,

Your OTP for email verification is:

{otp}

This OTP is valid for 5 minutes.

If you did not create this account, please ignore this email.

Thank you.
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )