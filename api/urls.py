
from django.urls import path, include
from . import views
urlpatterns = [
    # API endpoints
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),
]
