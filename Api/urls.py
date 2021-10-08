from django.urls import path
from . import views

urlpatterns = [
    path("course/", views.CourseAPIView.as_view()),
    path("difficulty/", views.DifficultyAPIView.as_view()),
    path("math/<int:course_id>/<int:difficulty_id>/", views.MathQAPIView.as_view()),
    path("info/", views.DifficultyAPIView.as_view()),
    path("withdraw/", views.DifficultyAPIView.as_view()),
]