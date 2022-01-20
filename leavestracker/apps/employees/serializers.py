from leavestracker.apps.employees.models import CustomUser
from rest_framework import serializers

class CustomEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email','first_name','last_name','username')