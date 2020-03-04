FROM python:alpine as builder

COPY qemu-*-static /usr/bin/

FROM builder

ARG VERSION=0.4.1
LABEL maintainer="Jay MOULIN <https://jaymoulin.me/femtopixel/github-release-notifier> <https://twitter.com/MoulinJay>"
LABEL version=${VERSION}

COPY . /app
WORKDIR /app

RUN pip install -U pip && \
    pip install -e . && \
    mkdir -p ${HOME}/.github_release_notifier && \
    touch ${HOME}/.github_release_notifier/versions

COPY ./entrypoint.sh /bin/entrypoint
COPY ./mycron.sh /bin/mycron
ENTRYPOINT ["/bin/entrypoint"]
CMD ["/bin/mycron"]
