FROM python:alpine3.6 as builder

COPY qemu-*-static /usr/bin/

FROM builder

ARG VERSION=0.3.2
LABEL maintainer="Jay MOULIN <jaymoulin@gmail.com> <https://twitter.com/MoulinJay>"
LABEL version=${VERSION}

RUN pip install -U pip && pip install github-release-notifier
COPY ./entrypoint.sh /bin/entrypoint
COPY ./mycron.sh /bin/mycron
ENTRYPOINT ["/bin/entrypoint"]
CMD ["/bin/mycron"]
