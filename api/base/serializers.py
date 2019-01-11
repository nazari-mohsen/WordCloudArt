from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from photography.models import thumbnail
from app.models import Help_App
from django.contrib.auth import get_user_model
User = get_user_model()


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = thumbnail
        fields = ('id', 'title', 'url')

class HelpListSerializer(ModelSerializer):
    class Meta:
        model = Help_App
        fields = ('url', )

class PhotoListSerializer(ModelSerializer):
    class Meta:
        model = thumbnail
        fields = ('id', 'cash', 'count', 'url')


class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False, allow_null=False)
    content = serializers.CharField(required=False, allow_blank=False, allow_null=False, max_length=150)
    cm = serializers.CharField(required=False, allow_blank=False, max_length=10, default='null')
    f = serializers.CharField(required=False, allow_blank=False, max_length=10, default='a')
    word1 = serializers.CharField(required=False, allow_blank=False, max_length=50)
    word2 = serializers.CharField(required=False, allow_blank=False, max_length=20)
    color1 = serializers.CharField(required=False, allow_blank=False, max_length=10, default='deepskyblue')
    color2 = serializers.CharField(required=False, allow_blank=False, max_length=10, default='crimson')
    main_color = serializers.CharField(required=False, allow_blank=False, max_length=10, default='gray')
    bg_color = serializers.CharField(required=False, allow_blank=False, max_length=10, default='white')

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('are', 'i', 'ar', 'ms', 'ad', 'br', 'iam')

class CoinSerializer(serializers.Serializer):
    imei = serializers.IntegerField(required=False, allow_null=False)

