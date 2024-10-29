from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employee
from django.contrib.auth.models import User

class EmployeeAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_employee(self):
        url = reverse('employee-list-create')
        data = {"name": "John Doe", "email": "john@example.com", "department": "Engineering", "role": "Developer"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_employees(self):
        url = reverse('employee-list-create')
        Employee.objects.create(name="John Doe", email="john@example.com")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_not_found(self):
        url = reverse('employee-detail', args=[999])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_employee(self):
        employee = Employee.objects.create(name="Jane Doe", email="jane@example.com")
        url = reverse('employee-detail', args=[employee.id])
        data = {"name": "Jane Smith"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Jane Smith")

    def test_delete_employee(self):
        employee = Employee.objects.create(name="Jane Doe", email="jane@example.com")
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
