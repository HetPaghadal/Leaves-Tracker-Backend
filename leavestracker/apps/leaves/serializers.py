from leavestracker.apps.leaves.models import Leaves
from rest_framework import serializers

class LeavesSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Leaves
        fields = ( 'user', 'start_date', 'end_date', 'reason', 'first_name', 'last_name', 'email')

    def validate(self, attrs):
        instance = Leaves(**attrs)
        instance.clean()
        return attrs
