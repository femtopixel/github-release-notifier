#!/bin/sh
set -e
# start-cron.sh

while [ true ]; do
    github-release-notifier
    sleep 1m
done
