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