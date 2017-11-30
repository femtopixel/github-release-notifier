#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, json, os
from github_release_notifier.parser import get_package
from pathlib import Path
from hashlib import sha224

__all__ = ['subscribe', 'unsubscribe', 'get', 'get_list']
__SALT__ = 'saltedUnique'
__DEFAULT_FILE__ = '~/.github_release_notifier/hooks'


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


def subscribe(package, callback, file=__DEFAULT_FILE__, salt=__SALT__):
    package = get_package(package)
    database = _get_database(file)
    try:
        database[package] = list(filter((callback).__ne__, database[package]))
        database[package].append(callback)
    except KeyError:
        database[package] = []
        database[package].append(callback)
    _set_database(database, file)
    return get_uuid(package, callback, salt)


def get_uuid(package, callback, salt=__SALT__):
    package = get_package(package)
    return sha224(callback.encode('utf-8') + package.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def unsubscribe(uuid, package, callback, file=__DEFAULT_FILE__, salt=__SALT__):
    package = get_package(package)
    database = _get_database(file)
    if uuid == get_uuid(package, callback, salt):
        database[package] = list(filter((callback).__ne__, database[package]))
    else:
        raise NameError('Wrong uuid for your package')
    _set_database(database, file)


def get(package, file=__DEFAULT_FILE__):
    package = get_package(package)
    database = _get_database(file)
    try:
        return database[package]
    except KeyError:
        return []


def get_list(file=__DEFAULT_FILE__):
    database = _get_database(file)
    return database.keys()


def main():
    print(subscribe(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
