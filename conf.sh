#!/bin/bash
cd /home/mohsen/PycharmProjects/new_wordcloud
/home/mohsen/PycharmProjects/new_wordcloud/venv/bin/celery -A cloud  worker --loglevel=info
