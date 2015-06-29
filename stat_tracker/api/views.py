from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
# Create your views here.

from .serializers import StatSerializer, ActivitySerializer
from .models import Stat, Activity
#from users.models import Profile

# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #pagination_class = StandardResultsSetPagination
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']