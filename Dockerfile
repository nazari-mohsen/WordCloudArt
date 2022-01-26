# ============= Builder Stage =============
FROM python:3.6-slim as builder
SHELL ["/bin/bash", "-c"]
# Set build-time variables
ARG APP_HOME=/usr/src
ARG PYTHON_VERSION=3.6.15
ARG DEBIAN_FRONTEND=noninteractive
ARG PIP_VERSION=21.3.1


# Set environment variables for build
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONPATH=${APP_HOME}

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev \
        build-essential \
        libpcre3 \
        libpcre3-dev \
        && \
    rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_HOME}

COPY --chown=builder:builder requirements.txt .

RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir --upgrade "pip==${PIP_VERSION}" wheel setuptools && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt uwsgi && \
    find /opt/venv -type d -name "__pycache__" -exec rm -rf {} + && \
    find /opt/venv -type f -name "*.pyc" -delete

# ============= Final Stage =============
FROM python:3.6-slim as runtime
SHELL ["/bin/bash", "-c"]
LABEL org.opencontainers.image.authors="Mohsen Nazari <mohsen.nazari@hotmail.com>" \
      org.opencontainers.image.description="wordcloud" \
      org.opencontainers.image.source="https://github.com/nazari-mohsen"
      
ARG APP_USER=app_user
ARG APP_HOME=/usr/src
ARG UWSGI_HTTP=:8000
ARG DEBIAN_FRONTEND=noninteractive

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    APP_HOME=${APP_HOME} \
    PYTHONPATH=${APP_HOME}/app \
    UWSGI_HTTP=${UWSGI_HTTP} \
    UWSGI_MODULE=${APP_USER}.wsgi:application \
    UWSGI_WORKERS=3 \
    UWSGI_THREADS=2 \
    UWSGI_MASTER=true \
    UWSGI_VACUUM=true \
    UWSGI_DIE_ON_TERM=true \
    UWSGI_MEMORY_REPORT=true \
    UWSGI_BUFFER_SIZE=32768 \
    UWSGI_MAX_REQUESTS=5000 \
    UWSGI_HARAKIRI=120 \
    UWSGI_RELOAD_ON_RSS=1024 


RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev \
        locales \
        gettext \
        && \
    sed -i '/en_US.UTF-8 UTF-8/s/^#//g' /etc/locale.gen && \
    locale-gen && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd -r ${APP_USER} && \
    useradd -r -g ${APP_USER} -d ${APP_HOME} ${APP_USER} && \
    mkdir -p ${APP_HOME}/{app,public/{media,static},logs} && \
    chown -R ${APP_USER}:${APP_USER} ${APP_HOME}

COPY --from=builder --chown=${APP_USER}:${APP_USER} /opt/venv /opt/venv
WORKDIR ${APP_HOME}/app
COPY --chown=${APP_USER}:${APP_USER} . ${APP_HOME}/app/

RUN chmod +x scripts/entrypoint.sh && \
    chmod -R 755 ${APP_HOME}/public 

USER ${APP_USER}
EXPOSE ${UWSGI_HTTP}

ENTRYPOINT ["scripts/entrypoint.sh"]

CMD ["uwsgi", "--ini", "scripts/uwsgi.ini"]