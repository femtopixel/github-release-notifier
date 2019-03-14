# coding: utf-8

import json
import os
from .parser import get_package
from pathlib import Path
from hashlib import sha224
from typing import KeysView

__SALT__ = 'saltedUnique'
__DEFAULT_FILE__ = os.getenv('GRN_HOOKS_FILE', str(Path.home()) + '/.github_release_notifier/hooks')


def _get_database(file: str = __DEFAULT_FILE__) -> dict:
    database = {}
    if Path(file).is_file():
        database = json.loads(open(file, "r").read())
    return database


def _set_database(database: dict, filepath: str = __DEFAULT_FILE__) -> None:
    dirname = os.path.dirname(filepath)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    file = open(filepath, "w+")
    file.write(json.dumps(database))
    file.close()


def subscribe(package: str, callback: str, file: str = __DEFAULT_FILE__, salt: str = __SALT__) -> str:
    package = get_package(package)
    database = _get_database(file)
    try:
        database[package] = list(filter(callback.__ne__, database[package]))
    except KeyError:
        database[package] = []
    database[package].append(callback)
    _set_database(database, file)
    return get_uuid(package, callback, salt)


def get_uuid(package: str, callback: str, salt: str = __SALT__) -> str:
    package = get_package(package)
    return sha224(callback.encode('utf-8') + package.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def unsubscribe(uuid: str, package: str, callback, file: str = __DEFAULT_FILE__, salt: str = __SALT__) -> None:
    package = get_package(package)
    database = _get_database(file)
    if uuid == get_uuid(package, callback, salt):
        database[package] = list(filter(callback.__ne__, database[package]))
    else:
        raise NameError('Wrong uuid for your package')
    _set_database(database, file)


def get(package: str, file: str = __DEFAULT_FILE__) -> dict:
    package = get_package(package)
    database = _get_database(file)
    return database.get(package, {})


def get_list(file: str = __DEFAULT_FILE__) -> KeysView:
    database = _get_database(file)
    return database.keys()
