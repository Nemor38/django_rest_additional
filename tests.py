from django.test import TestCase
from rest_framework.test import APIClient
from .models import Employee

class EmployeeTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.employee = Employee.objects.create(
            name="John Doe",
            position="Developer",
            vacation_days=3,
            working_days=22,
            holiday_days=8
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, "John Doe")
        self.assertEqual(self.employee.position, "Developer")

    def test_vacation_days_validation(self):
        response = self.client.post('/employees/', {'name': 'Jane Doe', 'vacation_days': 6})
        self.assertEqual(response.status_code, 400)

    def test_holiday_days_validation(self):
        response = self.client.post('/employees/', {'name': 'Jane Doe', 'holiday_days': 11})
        self.assertEqual(response.status_code, 400)
