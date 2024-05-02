FROM python:alpine

ARG VERSION=0.4.1
ARG TARGETPLATFORM
LABEL maintainer="Jay MOULIN <https://jaymoulin.me/femtopixel/github-release-notifier>"
LABEL version=${VERSION}-${TARGETPLATFORM}

COPY . /app
WORKDIR /app

RUN pip install -e . && \
    mkdir -p ${HOME}/.github_release_notifier && \
    touch ${HOME}/.github_release_notifier/versions

COPY ./entrypoint.sh /bin/entrypoint
COPY ./mycron.sh /bin/mycron
ENTRYPOINT ["/bin/entrypoint"]
CMD ["/bin/mycron"]
