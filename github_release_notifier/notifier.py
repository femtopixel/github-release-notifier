#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, os, requests, logging
from github_release_notifier.webhook import get, get_list
from github_release_notifier.parser import parse
from distutils.version import StrictVersion
from pathlib import Path

__DEFAULT_FILE__ = '/root/.github_release_notifier/versions'


def run(file=__DEFAULT_FILE__):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    updated = {}
    for package in get_list():
        for entry in parse(package):
            if StrictVersion(entry['version']) > StrictVersion(get_version(package)):
                database = _get_database(file)
                database[package] = entry['version']
                _set_database(database, file)
                updated[package] = entry['version']
                for webhook in get(package):
                    logger.info("Hook call : %s / %s" % (webhook, json.dumps(entry)))
                    try:
                        requests.post(webhook, dict(Body=json.dumps(entry)))
                    except:
                        logger.error("Error occured : %s" % (sys.exc_info()[0]))
                        pass
    return updated


def _get_database(file=__DEFAULT_FILE__):
    database = {}
    if Path(file).is_file():
        database = json.loads(open(file, "r").read())
    return database


def _set_database(database, filepath=__DEFAULT_FILE__):
    dirname = os.path.dirname(filepath)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    file = open(filepath, "w+")
    file.write(json.dumps(database))
    file.close()


def get_version(package, file=__DEFAULT_FILE__):
    database = _get_database(file)
    try:
        return database[package]
    except KeyError:
        return '0.0.0'


def main():
    print(run())


if __name__ == "__main__":
    main()
