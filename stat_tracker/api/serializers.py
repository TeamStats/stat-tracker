from rest_framework import serializers
from django.contrib.auth.models import User
import datetime
from .models import Activity, Stat
#from users.models import Profile

class StatSerializer(serializers.HyperlinkedModelSerializer):
    timestamp = serializers.DateField()
    url = serializers.HyperlinkedIdentityField(view_name='update_stat')

    class Meta:
        model = Stat
        fields = ('url', 'stat', 'timestamp', )

    def create(self, validated_data):
        stat = Stat.objects.create(**validated_data)
        stat.timestamp = datetime.date.today()
        stat.save()
        return stat


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(max_length=255)
    #user = serializers.HyperlinkedRelatedField(view_name='user-detail')
    stat_set = StatSerializer(many=True, read_only=True)
    stat = serializers.HyperlinkedIdentityField(view_name='create_stat')

    class Meta:
        model = Activity
        fields = ('url', 'title', 'stat_set', 'stat', )

