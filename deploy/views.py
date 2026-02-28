from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Teacher
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from .serializers import TeacherSerializer

class CustomPaginator(PageNumberPagination):
    page_size = 20


class TeacherListCreateApiVIew(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPaginator


class TeacherDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]
