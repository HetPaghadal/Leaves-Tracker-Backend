from django.contrib import admin
from django.urls import include, path
from leavestracker import views

urlpatterns = [
    path("", views.current_datetime),
    path("admin/", admin.site.urls),
    path("employees/", include("leavestracker.apps.employees.urls")),
    path("leaves/", include("leavestracker.apps.leaves.urls")),
]
