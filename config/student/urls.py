from django.urls import path

from .views import StudentDetailView, StudentListCreateView

urlpatterns = [
    path("", StudentListCreateView.as_view(), name="student-list-create"),
    path("<uuid:pk>/", StudentDetailView.as_view(), name="student-detail"),
]