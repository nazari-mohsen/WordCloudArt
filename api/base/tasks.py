from celery import task
from coin.models import Coin_video, Coin_price
from account.models import Profile
from log.models import Request_photo, CashCoin, Coinvideo, CreateUser
from photography.models import thumbnail
from log.models import Photo_log
from django.contrib.auth import get_user_model
from django.db.models import F
User = get_user_model()


@task
def Update_Coin_Profile(user, cash_coin):
    User0 = User.objects.filter(username=user).first()
    profile = Profile.objects.filter(user=User0).first()
    if profile.coin_video >= cash_coin:
        profile.coin_video = profile.coin_video - cash_coin
        profile.save()
    else:
        profile.coin_price = profile.coin_price - cash_coin
        profile.save()

@task
def Coin_video_save(time, user, cash_coin):
    user = User.objects.filter(username=user).first()
    video_coin = Coin_video()
    video_coin.user = user
    video_coin.coin_video = cash_coin
    video_coin.createDateTime = time
    video_coin.save()

@task
def Coin_price_save(time, user, orderId, cash_coin):
    user = User.objects.filter(username=user).first()
    price_coin = Coin_price()
    price_coin.user = user
    price_coin.orderId = orderId
    price_coin.coin_price = cash_coin
    price_coin.createDateTime = time
    price_coin.save()


@task
def Photo_count(time, user, id):
    user = User.objects.filter(username=user).first()
    Photo_id = thumbnail.objects.filter(id=id).first()
    Photo = Photo_log()
    Photo.user = user
    Photo.Photo = Photo_id
    Photo.createDateTime = time
    Photo.save()

    thumbnail.objects.filter(id=id).update(count=F('count') + 1)