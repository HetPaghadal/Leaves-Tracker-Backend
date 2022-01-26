from django.shortcuts import render
from leavestracker.apps.employees import constants as const
from leavestracker.apps.employees.models import CustomUser
from leavestracker.apps.employees.serializers import CustomEmployeesSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


class EmployeesView(APIView):
    serializer_class = CustomEmployeesSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                user = CustomUser.object.get(email=serializer.data['email'])
                token_obj , _ = Token.objects.get_or_create(user=user)
                data = {
                    'detail' : serializer.data,
                    'Token' : str(token_obj)
                }
                (data, response_status) = (data, status.HTTP_201_CREATED)
        except Exception as exc:
            if str(exc) == const.USERNAME_VALID_ERROR_MSG:
                user = CustomUser.objects.filter(
                    email=request.data['email']
                ).first()
                token_obj, _ = Token.objects.get_or_create(user=user)
                data = {
                    'detail' : CustomEmployeesSerializer(instance=user).data,
                    'Token' : str(token_obj)
                }
                (data, response_status) = (data, status.HTTP_200_OK)
            else:
                (data, response_status) = (
                    const.DEFAULT_ERROR,
                    status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(data, response_status)
