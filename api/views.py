from django.http import HttpResponse,JsonResponse
from .models import Task
from rest_framework.response import Response
from rest_framework.request import Request
from .serializer import TaskSerializer
from rest_framework.views import APIView


class TaskSet(APIView):
    def get(self,request):
        task = Task.objects.all()
        d = []
        for i in task:
            d.append(TaskSerializer(i).data)
        return Response(d)