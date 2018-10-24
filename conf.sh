#!/bin/bash
cd /home/mohsen/PycharmProjects/jwt
/home/mohsen/PycharmProjects/jwt/venv/bin/celery -A cloud  worker --loglevel=info
