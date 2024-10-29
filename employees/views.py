from django.shortcuts import render
from .models import Employee
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .serializers import EmployeeSerializer
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)

class EmployeePagination(PageNumberPagination):
    page_size = 10

class EmployeeListCreateView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        employees = Employee.objects.all()
        paginator = EmployeePagination()
        result_page = paginator.paginate_queryset(employees, request)
        serializer = EmployeeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Employee created successfully: {serializer.data['id']}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning("Failed to create due to validation issue")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class EmployeeDetailView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Employee updated successfully: {pk}")
            return Response(serializer.data)
        logger.warning(f"Failed to update employee: {pk}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        logger.info(f"Employee deleted {pk}")
        return Response(status=status.HTTP_204_NO_CONTENT)
