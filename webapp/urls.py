from django.urls import path
from .views import TaskPostGet,Taskputdelete

urlpatterns=[
    path('tasks/',TaskPostGet.as_view(),name='task-create'),
    path('tasks/<int:pk>/',Taskputdelete.as_view(),name='task-update'),
]