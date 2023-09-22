from .models import User, Lesson, Product, WatchStatus, Access
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'lessons']
        exclude = ['owner']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'url', 'length']


class WatchStatusSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    lesson = LessonSerializer()
    watched = serializers.IntegerField()
    watch_time = serializers.IntegerField()


class ProductStatsSerializer(serializers.Serializer):
    name = product_name = serializers.CharField()
    user_count = serializers.IntegerField()
    total_watch_time = serializers.IntegerField()
    watch_count = serializers.IntegerField()
