from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.http import HttpResponse
# Create your views here.
@api_view(['GET'])
def all_api_views(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<int:pk>/',
        'Create':'/create/',
        'Update':'/update-task/<int:pk>',
        'Delete':'/delete-task/<int:pk>'
    }
    
    return Response(api_urls)
@api_view(['GET'])
def detailTask(request,pk):
    try:
        task = Task.objects.get(id=pk)
    except:
        return HttpResponse("There is no task at particular ID!")
    serializer = TaskSerializer(task)
    return Response(serializer.data)
@api_view(['GET'])
def listTasks(request):
    tasks = Task.objects.all()[::-1]
    serializer = TaskSerializer(tasks, many = True)
    print(tasks)
    return Response(serializer.data)
@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance = task, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTask(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task Has been deleted successfully!")