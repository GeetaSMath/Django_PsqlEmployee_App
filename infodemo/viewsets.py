from rest_framework import viewsets
from .import models
from .import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.employee.objects.all()
    serializer_class = serializers.employeeSerializer

# list(), retrive(), create(), update(), delete()