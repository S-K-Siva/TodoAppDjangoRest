from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_api_views,name="api_urls"),
    path('create/',views.createTask,name="Create"),
    path('task-list/',views.listTasks,name="List"),
    path('update-task/<str:pk>',views.updateTask,name="Update"),
    path('delete-task/<str:pk>',views.deleteTask,name="Delete"),
    path('task-detail/<str:pk>/',views.detailTask,name="Detail View"),
]

