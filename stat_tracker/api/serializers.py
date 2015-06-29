from rest_framework import serializers
from django.contrib.auth.models import User
import datetime
from .models import Activity, Stat
#from users.models import Profile

class StatSerializer(serializers.Serializer):
    timestamp = serializers.DateField(read_only=True)
    activity = serializers.HyperlinkedRelatedField(read_only=True, view_name='activity-detail')

    class Meta:
        model = Activity
        fields = ('activity', 'stat', 'timestamp', )


class ActivitySerializer(serializers.Serializer):
    title = serializers.CharField()
    stat_set = StatSerializer(many=True)

    class Meta:
        model = Activity
        fields = ('text', 'stat_set', )
