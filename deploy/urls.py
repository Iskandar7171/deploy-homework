from django.urls import path
from .views import TeacherListCreateApiVIew, TeacherDetailApiView

urlpatterns = [
    path("teacher/", TeacherListCreateApiVIew.as_view()),
    path("teacher/detail/<int:pk>/", TeacherDetailApiView.as_view()),
]
