#!/bin/sh

set -e
if [ "${1#-}" != "$1" ]; then
    set -- github-release-notifier "$@"
fi

exec "$@"
