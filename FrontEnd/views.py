from django.shortcuts import render
from api.models import Task
# Create your views here.
def homepage(request):
    objects = Task.objects.all()
    print(objects)
    return render(request,"FrontEnd/index.html",context={"tasks":objects})