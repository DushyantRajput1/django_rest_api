from django.urls import include, path
from .views import UserListView , SignUpView , OTPVerificationView , LOGINView , UserListView

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("signup/" , SignUpView.as_view() , name="signup"),
    path("verify-otp/" , OTPVerificationView.as_view() , name="verify-otp"),
    path("login/" , LOGINView.as_view() , name="login") ,
    path("users/" , UserListView.as_view() , name="user-list") 
]

