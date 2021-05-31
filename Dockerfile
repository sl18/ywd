FROM ubuntu:latest AS project-base

LABEL maintainer="ashtart <ashtart@mail.ru>" \
      version="1.0" \
      description="Dup for Yandex Weather (test task)"

SHELL ["/bin/bash", "-c"]

# install base debs and dev utils:
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update                                           && \
    apt-get -y --no-install-recommends install apt-utils     && \
    apt-get -y --no-install-recommends install git curl wget    \
        locales build-essential software-properties-common      \
        unzip mc net-tools gpg-agent sqlite3                 && \
    locale-gen en_US.UTF-8 && dpkg-reconfigure locales


# local user to run under:
# install base debs and dev utils:
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update                                           && \
    apt-get -y --no-install-recommends install apt-utils     && \
    apt-get -y --no-install-recommends install git curl wget    \
        locales build-essential software-properties-common      \
        unzip mc net-tools gpg-agent sqlite3                 && \
    locale-gen en_US.UTF-8 && dpkg-reconfigure locales
# update base debs:
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y upgrade && apt-get -y dist-upgrade

# local user to run under:
ARG DEBIAN_FRONTEND=noninteractive
RUN adduser --shell /bin/bash --ingroup www-data --gecos "" --disabled-password testuser
USER testuser
RUN mkdir /home/testuser/tt-yw
USER root

# Python:
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y --no-install-recommends install python3 python3-pip python3-dev
USER testuser
RUN mkdir -p /home/testuser/tt-yw
COPY ya_weather /home/testuser/tt-yw/ya_weather
WORKDIR /home/testuser/tt-yw
USER root
COPY --chown=testuser:www-data requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt

RUN apt-get -y autoremove && apt-get -y clean && rm -rf /var/lib/apt/lists/*

# final adjustments:
RUN chown -R testuser:www-data /home/testuser/

ENV HOME /home/testuser

EXPOSE 8000
