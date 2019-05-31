# coding: utf-8

import feedparser
import re
import requests
from typing import List


def parse(package: str) -> List[dict]:
    package_name = get_package(package)
    url = 'https://github.com/%s/releases.atom' % package_name
    feed = feedparser.parse(url)
    entries = []
    for item in feed['entries']:
        current_dict = {
            'author': None,
            "content": None,
            "media": None,
            "date": item['updated_parsed'],
            "title": item['title_detail']['value'],
            "version": re.search('(?<=Repository/)[0-9]+/(.+)', item['id']).group(1),
            "package_name": package_name,
        }
        if 'authors' in item and item['authors'][0] is not None and 'name' in item['authors'][0]:
            current_dict['author'] = item['authors'][0]['name']
        if 'content' in item and item['content'][0] is not None and 'value' in item['content'][0]:
            current_dict['content'] = item['content'][0]['value']
        if (
            'media_thumbnail' in item and
            item['media_thumbnail'][0] is not None
            and 'url' in item['media_thumbnail'][0]
        ):
            current_dict['media'] = item['media_thumbnail'][0]['url']
        entries.append(current_dict)
    return entries


def get_package(entry: str) -> str:
    if 'github' in entry:
        entry = re.search('(?<=github.com/)[^/]+/[^/]+', entry).group(0)
    request = requests.get('https://github.com/%s/tags.atom' % entry)
    if request.status_code != 200:
        raise NameError('%s is not a valid github url/package' % entry)
    return entry
