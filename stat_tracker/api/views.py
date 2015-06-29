import datetime
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)


class StatListCreateView(generics.ListCreateAPIView):
    serializer_class = StatSerializer

    def initial(self, request, *args, **kwargs):
        self.activity = Activity.objects.get(pk=kwargs['pk'])
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return Stat.objects.filter(activity__id=self.kwargs['pk'])

    def perform_create(self, serializer):
        serializer.save(activity=self.activity)


class StatUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StatSerializer
    queryset = Stat.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
