from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import StudentSerializer
from api.models import Student
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response({'message': 'Data retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response({'message': 'Data retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Error creating data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = request.data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Error updating data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = request.data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data partially updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Error partially updating data', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = request.data.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        return Response({'message': 'Data deleted successfully'}, status=status.HTTP_200_OK)
