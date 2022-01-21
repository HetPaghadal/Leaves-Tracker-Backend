from django.shortcuts import render
from leavestracker.apps.employees import constants as const
from leavestracker.apps.employees.models import CustomUser
from leavestracker.apps.employees.serializers import CustomEmployeesSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class EmployeesView(APIView):
    serializer_class = CustomEmployeesSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                (data, response_status) = (serializer.data, status.HTTP_201_CREATED)
        except Exception as exc:
            if str(exc) == const.USERNAME_VALID_ERROR_MSG:
                queryset = CustomUser.objects.filter(
                    username=serializer.data["username"]
                ).first()
                (data, response_status) = (
                    CustomEmployeesSerializer(instance=queryset).data,
                    status.HTTP_200_OK,
                )
            else:
                (data, response_status) = (
                    const.DEFAULT_ERROR,
                    status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(data, response_status)
