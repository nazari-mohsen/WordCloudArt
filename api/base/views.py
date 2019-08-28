# -*- coding: utf-8 -*-
from rest_framework import generics
from .serializers import PhotoListSerializer, PhotoSerializer, CreateUserSerializer,\
    CoinSerializer, CategoryListSerializer, HelpListSerializer, Photo_v2Serializer
from django_filters.rest_framework import DjangoFilterBackend
from photography.models import thumbnail
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from category.models import Category
from ap.create_photo import create_photo
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from pprint import pprint
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework_jwt.settings import api_settings
from rest_framework.views import APIView
from django.db.models import F
from datetime import datetime
from .tasks import Coin_video_save, Photo_count, Coin_price_save, Update_Coin_Profile
from log.tasks import request_photo, cashcoin, coinvideo, createuser, crash
from app.models import version, Help_App
from account.models import Profile
from django.utils.crypto import get_random_string
from coin.models import Coin_price
import uuid

cash_coin_video = 100
cash_coin = 100
PREFIX = getattr(settings, "PREFIX", None)
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()

# def create_token(user):
#     payload = jwt_payload_handler(user)
#     return jwt_encode_handler(payload)
packagename = "ir.yildizlar.sheklekalemeha"
# developerpayload = "payload-string"
Key_bazar = "MIHNMA0GCSqGSIb3DQEBAQUAA4G7ADCBtwKBrwDcyJOhI46b1Y6wjoeHbP3/tqWz9GnrLjJsTyjAXB/oZW+lSAmvEFycr3AyxWLnzZvMbI0JWemVLjqGVkZFCb/8YAKHVrRykeaAVOiJUm5jYB0Yqhwj0XUdvldBeN2clX3RoNDwBo/M8VndtZbr/+BuKnBLm4ns1LkO98oZbt1o8CI+o8x+cwNCmful5Ai0H91s4nnywGNhCLRU0+yCA0AEpmmxPY96q/EfXtUKdcECAwEAAQ=="


class HelpListAPIView(generics.ListAPIView):
    serializer_class = HelpListSerializer
    def get_queryset(self):
        cache_key = 'Help'
        result = cache.get(cache_key, None)
        if not result:
            result = Help_App.objects.filter(status="1").distinct().order_by('-order')
            cache.set(cache_key, result, timeout=CACHE_TTL)
        return result

class categoryListAPIView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)
    def get_queryset(self):
        cache_key = 'category'
        result = cache.get(cache_key, None)
        if not result:
            result = Category.objects.filter(status="1").distinct().order_by('-order')
            cache.set(cache_key, result, timeout=CACHE_TTL)
        return result

class ColorListAPIView(APIView):
    def get(self, request):
        color = {"a": "FA8072", "b": "DA70D6", "c": "98FB98", "d": "FFFFE0"}
        return Response(color)


class photoListAPIView(generics.ListAPIView):
    serializer_class = PhotoListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category',)
    def get_queryset(self):
        cache_key = 'photo'
        result = cache.get(cache_key, None)
        if not result:
            result = thumbnail.objects.filter(status="1").distinct().order_by('-order')
            cache.set(cache_key, result, timeout=CACHE_TTL)
        return result

class categoryListDevelopAPIView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)
    def get_queryset(self):
        cache_key = 'categorydevelop'
        result = cache.get(cache_key, None)
        if not result:
            result = Category.objects.all().distinct().order_by('-order')
            cache.set(cache_key, result, timeout=CACHE_TTL)
        return result

class photoListDevelopAPIView(generics.ListAPIView):
    serializer_class = PhotoListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category',)
    def get_queryset(self):
        cache_key = 'photodevelop'
        result = cache.get(cache_key, None)
        if not result:
            result = thumbnail.objects.filter(status="0").distinct().order_by('-order')
            cache.set(cache_key, result, timeout=CACHE_TTL)
        return result

class CkeckVersionAPIView(APIView):
    def get(self, request):
        cache_key = 'version'
        result = cache.get(cache_key, None)
        if not result:
            result = version.objects.get(status="1")
            cache.set(cache_key, result, timeout=CACHE_TTL)
        ver = {"ver": result.ver}
        return Response(ver)

class KeyAPIView(APIView):
    def get(self, request):
        print(request.user)
        payload = get_random_string(length=15)
        cache.set(request.user, payload, timeout=86400)
        key = {"key": Key_bazar, "pl": payload}
        return Response(key)

class CkeckCoinAPIView(APIView):
    def get(self, request):
        message = {"status": "Error"}
        user = User.objects.filter(username=request.user).first()
        if user:
            result = Profile.objects.filter(user_id=user.id).first()
            if result:
                coin = {"coin": result.coin, "cv": cash_coin_video}
                return Response(coin)
            else:
                return Response({"coin": "0", "cv": cash_coin_video})
        else:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        message = {"status": "Error"}
        print(request.data)
        coinvideo(str(request.user), request.data)
        serializer = CoinSerializer(data=request.data)
        if serializer.is_valid():
            imei = serializer.data.get('imei')
            user = Profile.objects.filter(user=request.user).first()
            if user:
                user.coin_video = user.coin_video + cash_coin_video
                user.coin = user.coin + cash_coin_video
                user.save()
                Coin_video_save.delay(datetime.now(), str(request.user), cash_coin_video)
                return Response({"coin": user.coin})
            else:
                instance = User.objects.filter(username=request.user).first()
                profile = Profile()
                profile.user = instance
                profile.coin = cash_coin_video
                profile.coin_video = cash_coin_video
                profile.save()
                Coin_video_save.delay(datetime.now(), str(request.user), cash_coin_video)
                return Response({
                    "coin": profile.coin
                })
        else:
            return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

class CashCoinAPIView(APIView):
    def post(self, request):
        print(request.user)
        print(request.data)
        cashcoin(str(request.user), request.data)
        requs = request.data
        developerpayload = cache.get(request.user, None)
        try:
            #Sku = requs['purchase']['mSku']
            #PackageName = requs['purchase']['mPackageName']
            #time = requs['purchase']['mPurchaseTime']
            #Payload = requs['purchase']['mDeveloperPayload']
            #orderId = requs['purchase']['mOrderId']
            Sku = requs['purchase']['d']
            PackageName = requs['purchase']['c']
            time = requs['purchase']['e']
            #Payload = requs['purchase']['g']
            orderId = requs['purchase']['h']
            if Sku and PackageName and time and orderId:
                if PackageName == packagename:
                    choices = {'seke1': 1000, 'seke2': 2000, 'seke3': 4000, 'seke4': 8000}
                    cash = choices.get(Sku)
                    profile = Profile.objects.filter(user=request.user).first()
                    if profile:
                        profile.coin_price = profile.coin_price + cash
                        profile.coin = profile.coin + cash
                        profile.save()
                        Coin_price_save.delay(time, str(request.user), orderId, cash)
                        return Response({
                            "coin": profile.coin
                        })
                    else:
                        instance = User.objects.filter(username=request.user).first()
                        profile = Profile()
                        profile.user = instance
                        profile.coin = cash
                        profile.coin_price = cash
                        profile.save()
                        Coin_price_save.delay(time, str(request.user), orderId, cash)
                        return Response({
                            "coin": profile.coin
                        })
                else:
                    return Response({"status": "invalid data"}, status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response({"status": "not found json data"}, status.HTTP_404_NOT_FOUND)
        except:
            return Response({"status": "invalid format json"}, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def PhotoAPIView(request):
    print(request.data)
    print(request.user)
    usern = str(request.user)
    request_photo(usern, request.data)
    user = User.objects.filter(username=request.user).first()
    if user:
        result = Profile.objects.filter(user_id=user.id).first()
        if result:
            serializer = PhotoSerializer(data=request.data)
            if serializer.is_valid():
                id = serializer.data.get('id')
                content = serializer.data.get('content')
                colormap = serializer.data.get('cm')
                font = serializer.data.get('f')
                word1 = serializer.data.get('word1')
                word2 = serializer.data.get('word2')
                color1 = serializer.data.get('color1')
                color2 = serializer.data.get('color2')
                main_color = serializer.data.get('main_color')
                bg_color = serializer.data.get('bg_color')
                if id and content:
                    cache_key = 'photo_main' + str(id)
                    photo_main = cache.get(cache_key, None)
                    if not photo_main:
                        photo_main = thumbnail.objects.filter(id=id).first()
                    if photo_main is not None and result.coin >= photo_main.cash:
                        cache.set(cache_key, photo_main, timeout=CACHE_TTL)
                        url_image = create_photo(id, content, colormap, font, word1, word2, color1, color2, main_color, bg_color, usern)
                        Photo_count.delay(datetime.now(), usern, id)
                        Profile.objects.filter(user=request.user).update(coin=F('coin') - photo_main.cash)
                        Update_Coin_Profile.delay(usern, int(photo_main.cash))
                        res = url_image
                        profile = Profile.objects.get(user=request.user)
                        res["coin"] = profile.coin
                        return Response(res, status=status.HTTP_200_OK)
                    else:
                        return Response({"ERROR": "User Not Enough Coin"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"ERROR": "User Not Coin"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"ERROR": "User Not Found Coin"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Photo_v2APIView(request):
    # print(request.data)
    # print(request.user)
    usern = str(request.user)
    request_photo(usern, request.data)
    user = User.objects.filter(username=request.user).first()
    if user:
        result = Profile.objects.filter(user_id=user.id).first()
        if result:
            serializer = Photo_v2Serializer(data=request.data)
            if serializer.is_valid():
                id = serializer.data.get('id')
                content = serializer.data.get('content')
                colormap = serializer.data.get('cm')
                font = serializer.data.get('f')
                word1 = serializer.data.get('word1')
                word2 = serializer.data.get('word2')
                color1 = serializer.data.get('color1')
                color2 = serializer.data.get('color2')
                main_color = serializer.data.get('main_color')
                bg_color = serializer.data.get('bg_color')
                if id and content:
                    cache_key = 'photo_main' + str(id)
                    photo_main = cache.get(cache_key, None)
                    if not photo_main:
                        photo_main = thumbnail.objects.filter(id=id).first()
                    if photo_main is not None and result.coin >= photo_main.cash:
                        cache.set(cache_key, photo_main, timeout=CACHE_TTL)
                        url_image = create_photo(id, content, colormap, font, word1, word2, color1, color2, main_color, bg_color, usern)
                        Photo_count.delay(datetime.now(), usern, id)
                        Profile.objects.filter(user=request.user).update(coin=F('coin') - photo_main.cash)
                        Update_Coin_Profile.delay(usern, int(photo_main.cash))
                        res = url_image
                        profile = Profile.objects.get(user=request.user)
                        res["coin"] = profile.coin
                        return Response(res, status=status.HTTP_200_OK)
                    else:
                        return Response({"ERROR": "User Not Enough Coin"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"ERROR": "User Not Coin"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"ERROR": "User Not Found Coin"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((AllowAny, ))
def CreateUserAPIView(request):
    message = {"status": "Error"}
    createuser(request.data)
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        # pprint(serializer)
        # now = str(datetime.now().second)
        # username = 'user' + now + get_random_string(length=10)
        username = uuid.uuid4()
        # pprint(username)
        password = User.objects.make_random_password()
        android_id = serializer.data.get('ad')
        mac_address = serializer.data.get('ms')
        android_ver = serializer.data.get('ar')
        app_ver_code = serializer.data.get('are')
        im_id_mac = serializer.data.get('iam')
        imei = serializer.data.get('i')
        adnroid_brand = serializer.data.get('br')
        market = serializer.data.get('mr')
        user = User.objects.filter(i=imei, ad=android_id).first()
        if not user:
            user = User.objects.create_user(username=username, ad=android_id, i=imei,
                                        password=password, Password_user=password,
                                            ar=android_ver, are=app_ver_code,
                                            ms=mac_address, iam=im_id_mac, br=adnroid_brand, mr=market)

            user.save()
            instance = User.objects.filter(username=username).first()
            profile = Profile()
            profile.user = instance
            profile.coin = cash_coin
            profile.coin_video = cash_coin
            profile.save()
            Coin_video_save.delay(datetime.now(), str(request.user), cash_coin)
            return Response({"ps": password, "ur": username})
        else:
            user.are = app_ver_code
            user.br = adnroid_brand
            user.mr = market
            user.save()
            ps = user.Password_user
            ur = user.username
            return Response({"ps": ps, "ur": ur})

    return Response(message, status=status.HTTP_400_BAD_REQUEST)


class CrashAPIView(APIView):
    def post(self, request):
        print(request.user)
        print(request.data)
        crash(request.data, str(request.user))
        return Response(status=status.HTTP_200_OK)
