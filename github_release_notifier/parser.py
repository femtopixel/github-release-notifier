#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, feedparser, re, requests

__all__ = ['parse', 'get_package']


def parse(package):
    package_name = get_package(package)
    url = 'https://github.com/%s/releases.atom' % package_name
    feed = feedparser.parse(url)
    entries = []
    for item in feed['entries']:
        entries.append({
            "author": item['authors'][0]['name'] if 'authors' in item and item['authors'] and item['authors'][0] and item['authors'][0]['name'] else None,
            "date": item['updated_parsed'],
            "title": item['title_detail']['value'],
            "content": item['content'][0]['value'] if 'content' in item and  item['content'] and item['content'][0] and item['content'][0]['value'] else None,
            "version": re.search('(?<=Repository/)[0-9]+/(.+)', item['id']).group(1),
            "media": item['media_thumbnail'][0]['url'] if 'media_thumbnail' in item and item['media_thumbnail'] and item['media_thumbnail'][0] and item['media_thumbnail'][0]['url'] else None,
            "package_name": package_name,
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
