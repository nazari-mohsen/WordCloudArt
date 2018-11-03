from celery import task
from .models import Request_photo, CashCoin, Coinvideo, CreateUser, Crash
from django.contrib.auth import get_user_model

User = get_user_model()

@task
def request_photo(user, log):
    # log0 = str(log)
    user = User.objects.filter(username=user).first()
    request_photo = Request_photo()
    request_photo.user = user
    request_photo.log = log
    # video_coin.createDateTime = time
    request_photo.save()

@task
def cashcoin(user, log):
    # log0 = str(log)
    user = User.objects.filter(username=user).first()
    cashcoin = CashCoin()
    cashcoin.user = user
    cashcoin.log = log
    # video_coin.createDateTime = time
    cashcoin.save()

@task
def coinvideo(user, log):
    # log0 = str(log)
    user = User.objects.filter(username=user).first()
    coinvideo = Coinvideo()
    coinvideo.user = user
    coinvideo.log = log
    # video_coin.createDateTime = time
    coinvideo.save()

@task
def createuser(log):
    # log0 = str(log)
    # user = User.objects.filter(username=user).first()
    createuser = CreateUser()
    # coinvideo.user = user
    createuser.log = log
    # video_coin.createDateTime = time
    createuser.save()

@task
def crash(log, user):
    crash = Crash()
    crash.user = user
    crash.log = log
    crash.save()