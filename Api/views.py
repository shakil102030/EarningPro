from django.shortcuts import render
from rest_framework import permissions, status
from .models import Course, Difficulty, MathQ
from .serializers import CourseSerializers, DifficultySerializers, MathQSerializers, InfoSerializers, WithdrawSerializers
from rest_framework.views import APIView
from rest_framework.response import Response

class CourseAPIView(APIView):
    def get(self, request, format=None):
        result = Course.objects.all()
        serialize = CourseSerializers(result, many = True)
        return Response(serialize.data, status=status.HTTP_201_CREATED)

class DifficultyAPIView(APIView):
    def get(self, request, format=None):
        result = Difficulty.objects.all()
        serialize = DifficultySerializers(result, many = True)
        return Response(serialize.data, status=status.HTTP_201_CREATED)

class MathQAPIView(APIView):
    def get(self, request, course_id, difficulty_id,  format=None):
        result = MathQ.objects.filter(course_id=course_id, difficulty_id=difficulty_id)
        serialize = MathQSerializers(result, many = True)
        return Response(serialize.data, status=status.HTTP_201_CREATED)


class InfoAPIView(APIView):
    def get(self, request, course_id, difficulty_id,  format=None):
        result = Info.objects.filter(course_id=course_id, difficulty_id=difficulty_id)
        serialize = InfoSerializers(result, many = True)
        return Response(serialize.data, status=status.HTTP_201_CREATED)

class WithdrawAPIView(APIView):
    def post(self, request):
        serializer = WithdrawSerializers(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)