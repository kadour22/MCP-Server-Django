from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from .tools.mcp_tools import TOOLS

class mcp_tools_view(APIView):
    def get(self, request, format=None):
        tools_list = TOOLS
        return Response(tools_list, status=status.HTTP_200_OK)

class MCPInvokeView(APIView):
    def post(self, request):
        name = request.data.get("name")
        args = request.data.get("arguments", {})
        if name == "task_create":
            serializer = TaskSerializer(data=args)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.ok(serializer.data)
        if name == "task_list":
            qs = Task.objects.all()
            data = TaskSerializer(qs, many=True).data
            return self.ok(data)
        if name == "task_get":
            task = Task.objects.get(id=args["id"])
            return self.ok(TaskSerializer(task).data)
        if name == "task_update":
            task = Task.objects.get(id=args["id"])
            serializer = TaskSerializer(task, data=args, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.ok(serializer.data)
        if name == "task_delete":
            Task.objects.filter(id=args["id"]).delete()
            return self.ok({"deleted": True})
        return Response(
            {"error": "Unknown tool"},
            status=status.HTTP_400_BAD_REQUEST
        )

    def ok(self, data):
        return Response({
            "content": [
                {
                    "type": "json",
                    "data": data
                }
            ]
        })

