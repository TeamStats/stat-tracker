from rest_framework import serializers
from django.contrib.auth.models import User
import datetime
from .models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    #activity = serializers.HyperlinkedRelatedField(view_name='activity-detail', read_only=True)

    class Meta:
        model = User
        fields = ('username', 'url',)


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')

    class Meta:
        model = Profile
        fields = ('id', 'location', 'age', 'interests', 'user')
