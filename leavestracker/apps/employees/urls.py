from django.urls import path
from leavestracker.apps.employees.views import EmployeesView

urlpatterns = [
    path('employees/', EmployeesView.as_view(), name='employee'),
]