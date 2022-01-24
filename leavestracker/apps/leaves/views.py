from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
from leavestracker.apps.leaves import constants as const
from leavestracker.apps.leaves.models import Leaves
from leavestracker.apps.leaves.serializers import LeavesSerializer
from leavestracker.apps.employees.models import CustomUser
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import datetime

class LeavesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = LeavesSerializer

    def get(self, request):
        today = datetime.date.today()
        if "date" in request.GET:
            queryset = Leaves.objects.filter(
                start_date__lte=request.GET["date"], end_date__gte=request.GET["date"]
            )
        else:
            queryset = Leaves.objects.filter(
                end_date__gte=today
            ).order_by('start_date')
        (data, response_status) = (
            LeavesSerializer(instance=queryset, many=True).data,
            status.HTTP_200_OK,
        )

        data = []
        for e in queryset:
            object = {}
            object['name'] = e.user.first_name + ' ' + e.user.last_name
            object['start_date'] = e.start_date
            object['end_date'] = e.end_date
            object['reason'] = e.reason
            data.append(object)

        return Response(data, response_status)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                (data, response_status) = (
                    const.LEAVE_SUCCESS_MSG,
                    status.HTTP_201_CREATED,
                )
        except Exception as exc:
            if str(exc) == const.DUPLICATE_LEAVE_ERROR:
                (data, response_status) = (
                    const.DUPLICATE_LEAVE_MSG,
                    status.HTTP_409_CONFLICT,
                )
            elif str(exc) == const.INVALID_DATE_ERROR:
                (data, response_status) = (
                    const.INVALID_DATE_MSG,
                    status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            else:
                (data, response_status) = (
                    const.DEFAULT_ERROR,
                    status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(data, response_status)
