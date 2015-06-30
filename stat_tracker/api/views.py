import datetime
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers

from .serializers import StatSerializer, ActivitySerializer, UserSerializer
from .models import Stat, Activity
#from users.models import Profile

# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Activity.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatListCreateView(generics.ListCreateAPIView):
    serializer_class = StatSerializer

    def initial(self, request, *args, **kwargs):
        self.activity = Activity.objects.get(pk=kwargs['pk'])
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return Stat.objects.filter(activity__id=self.kwargs['pk'])

    def perform_create(self, serializer):
        same_act = Stat.objects.filter(activity=self.activity)
        if same_act:
            for stat in same_act:
                if stat.timestamp == serializer.validated_data['timestamp']:
                    raise serializers.ValidationError("Entry all ready exists for that day, please edit existing entry.")

        serializer.save(activity=self.activity)


class StatUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StatSerializer
    queryset = Stat.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = User.objects.filter(pk=self.request.user.pk)
        return queryset

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user.profile)
