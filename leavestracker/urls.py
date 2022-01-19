from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('leavestracker.apps.employees.urls')),
#
]
