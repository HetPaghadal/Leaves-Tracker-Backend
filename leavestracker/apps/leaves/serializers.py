from django.core.exceptions import ValidationError
from leavestracker.apps.leaves.models import Leaves
from rest_framework import serializers

class LeavesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leaves
        fields = ( 'id', 'user','start_date','end_date','reason')

    def validate(self, attrs):
        instance = Leaves(**attrs)
        instance.clean()
        return attrs