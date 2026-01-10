from django.urls import path
from . import views

urlpatterns = [
    path('mcp-tools/', views.mcp_tools_view.as_view(), name='mcp-tools'),
]