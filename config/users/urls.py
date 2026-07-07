from django.urls import include, path
from .views import UserListView , SignUpView

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("signup/" , SignUpView.as_view() , name="signup")
]
