from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from photography.models import thumbnail
from django.contrib.auth import get_user_model
User = get_user_model()


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = thumbnail
        fields = ('id', 'title', 'url')

class PhotoListSerializer(ModelSerializer):
    class Meta:
        model = thumbnail
        fields = ('id', 'cash', 'count', 'url')


class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=False)
    content = serializers.CharField(required=False, allow_blank=False, allow_null=False, max_length=150)
    word1 = serializers.CharField(required=False, allow_blank=False, max_length=50)
    word2 = serializers.CharField(required=False, allow_blank=False, max_length=20)
    color1 = serializers.CharField(required=False, allow_blank=False, max_length=10, default='deepskyblue')
    color2 = serializers.CharField(required=False, allow_blank=False, max_length=10, default='crimson')
    main_color = serializers.CharField(required=False, allow_blank=False, max_length=10, default='default')
    bg_color = serializers.CharField(required=False, allow_blank=False, max_length=10, default='white')

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('are', 'i', 'ar', 'ms', 'ad', 'iam')

class CoinSerializer(serializers.Serializer):
    imei = serializers.IntegerField(required=False, allow_null=False)

