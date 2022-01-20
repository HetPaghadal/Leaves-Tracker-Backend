from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from leavestracker.apps.leaves import constants as const
from leavestracker.apps.leaves.models import Leaves
from leavestracker.apps.leaves.serializers import LeavesSerializer
from leavestracker.apps.employees.models import CustomUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class LeavesView(APIView):
    serializer_class = LeavesSerializer

    def get(self,request,date=None):
        if 'date' in request.GET:
            queryset = Leaves.objects.filter(start_date__lte=request.GET['date']).filter(end_date__gte=request.GET['date'])
        else:
            queryset = Leaves.objects.all()
        (data, response_status) = (LeavesSerializer(instance=queryset, many=True).data, status.HTTP_200_OK)
        return Response(data, response_status)

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                (data, response_status) = (const.SUCCESS_MSG , status.HTTP_201_CREATED)
        except Exception as exc:
            print(exc)
            if str(exc)==const.DUPLICATE_ENTRY_ERROR:
                (data, response_status) = (const.DUPLICATE_ENTRY_MSG, status.HTTP_208_ALREADY_REPORTED)
            elif str(exc)==const.INVALID_DATE_ERROR:
                (data, response_status) = (const.INVALID_DATE_MSG, status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                (data, response_status) = (const.DEFAULT_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data, response_status)