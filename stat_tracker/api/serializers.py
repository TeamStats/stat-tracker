from rest_framework import serializers
from django.contrib.auth.models import User
import datetime
from .models import Activity, Stat
#from users.models import Profile
from rest_framework.validators import UniqueTogetherValidator


class StatSerializer(serializers.HyperlinkedModelSerializer):
    timestamp = serializers.DateField()
    url = serializers.HyperlinkedIdentityField(view_name='update_stat')
    #activity = serializers.HyperlinkedRelatedField(view_name='activity-detail', read_only=True)

    class Meta:
        model = Stat
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Stat.objects.all(),
        #         fields=('timestamp', 'activity')
        #     )
        # ]
        fields = ('url', 'stat', 'timestamp', )

    # def create(self, validated_data):
    #     stat = Stat.objects.create(**validated_data)
    #     stat.answer = validated_data[]
    #     stat.save()
    #     return stat

    # def validate(self, attrs):



class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(max_length=255)
    #user = serializers.HyperlinkedRelatedField(view_name='user-detail')
    stat_set = StatSerializer(many=True, read_only=True)
    stat = serializers.HyperlinkedIdentityField(view_name='create_stat')

    class Meta:
        model = Activity
        fields = ('url', 'title', 'stat_set', 'stat', )

