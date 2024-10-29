from rest_framework import serializers
from . models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

    def validate_email(self,value):
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use")
        
        return value
    
    def validate_name(self,value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty or should not have whitespace")

        return value