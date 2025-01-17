from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import HasPositionPermission

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [HasPositionPermission]
