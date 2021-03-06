from rest_framework import serializers
import datetime
from .models import Activity, Stat
from rest_framework.validators import UniqueTogetherValidator


class StatSerializer(serializers.HyperlinkedModelSerializer):
    timestamp = serializers.DateField()
    url = serializers.HyperlinkedIdentityField(view_name='update_stat')

    class Meta:
        model = Stat
        fields = ('url', 'id', 'stat', 'timestamp', )



class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(max_length=255)
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    stat_set = StatSerializer(many=True, read_only=True)
    stat = serializers.HyperlinkedIdentityField(view_name='create_stat')

    class Meta:
        model = Activity
        fields = ('url', 'id', 'user', 'title', 'stat_set', 'stat',)


