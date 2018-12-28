FROM python:alpine3.6 as builder

COPY qemu-*-static /usr/bin/

FROM builder

LABEL maintainer="Jay MOULIN <jaymoulin@gmail.com> <https://twitter.com/MoulinJay>"

RUN pip install -U pip && pip install github-release-notifier
COPY ./entrypoint.sh /bin/entrypoint
COPY ./mycron.sh /bin/mycron
ENTRYPOINT ["/bin/entrypoint"]
CMD ["/bin/mycron"]
