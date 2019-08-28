from celery import task
import os
import shutil
from datetime import datetime
from cloud.settings import MEDIA_ROOT

path = MEDIA_ROOT + 'user/'
date = datetime.now().strftime('%Y%m%d')


@task
def photo_remove(save_place, user):

    user_dir = path + user + '/' + date + '/photo'
    if os.path.exists(save_place):
        if os.path.exists(user_dir):
            shutil.move(save_place, user_dir)
        else:
            os.makedirs(user_dir)
            shutil.move(save_place, user_dir)
    else:
        pass
