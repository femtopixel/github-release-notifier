#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import github_release_notifier


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", '-a',
                        default='cron',
                        choices=['cron', 'subscribe', 'unsubscribe'],
                        help="Action to do (default: cron)")
    parser.add_argument("--package", '-p',
                        help="Github package name / url (required for subscribe/unsubscribe) - prints uuid on subscription")
    parser.add_argument("--webhook", '-w', help="URL to your webhook (required for subscribe/unsubscribe)")
    parser.add_argument("--uuid", '-u', help="UUID of your webhook (required for unsubscribe)")
    args = parser.parse_args()
    if args.action == 'cron':
        print(github_release_notifier.notifier.run())
    if args.action == 'subscribe':
        print(github_release_notifier.webhook.subscribe(args.package, args.webhook))
    if args.action == 'unsubscribe':
        github_release_notifier.webhook.unsubscribe(args.uuid, args.package, args.webhook)


if __name__ == "__main__":
    main()
