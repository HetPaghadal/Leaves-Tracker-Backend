from django.urls import path
from leavestracker.apps.leaves.views import LeavesView


urlpatterns = [
    path('leaves/', LeavesView.as_view(), name='employee'),
    # path('leaves/<int:date>', )
]