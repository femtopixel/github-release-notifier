#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, feedparser, re, datetime, requests

__all__ = ['parse', 'get_package']


def parse(package):
    url = 'https://github.com/%s/tags.atom' % get_package(package)
    feed = feedparser.parse(url)
    entries = []
    for item in feed['entries']:
        entries.append({
            "author": item['authors'][0]['name'],
            "date": item['updated_parsed'],
            "title": item['title_detail']['value'],
            "content": item['content'][0]['value'],
            "version": re.search('(?<=Repository/)[0-9]+/(.+)', item['id']).group(1),
            "media": item['media_thumbnail'][0]['url'],
        })
    return entries


def get_package(entry):
    if 'github' in entry:
        entry = re.search('(?<=github.com/)[^/]+/[^/]+', entry).group(0)
    request = requests.get('https://github.com/%s/tags.atom' % entry)
    if request.status_code != 200:
        raise NameError('%s is not a valid github url/package' % entry)
    return entry


def main():
    print(parse(sys.argv[1]))


if __name__ == "__main__":
    main()
