.. image:: https://github.com/femtopixel/github-release-notifier/raw/master/logo.png

=======================
Github Release Notifier
=======================

.. image:: https://img.shields.io/github/release/femtopixel/github-release-notifier.svg
    :alt: latest release
    :target: http://github.com/femtopixel/github-release-notifier/releases
.. image:: https://img.shields.io/pypi/v/github-release-notifier.svg
    :alt: latest release
    :target: https://pypi.org/project/github-release-notifier/
.. image:: https://img.shields.io/docker/pulls/femtopixel/github-release-notifier.svg
    :alt: Docker pull
    :target: https://hub.docker.com/r/femtopixel/github-release-notifier/
.. image:: https://img.shields.io/docker/stars/femtopixel/github-release-notifier.svg
    :alt: Docker stars
    :target: https://hub.docker.com/r/femtopixel/github-release-notifier/
.. image:: https://github.com/jaymoulin/jaymoulin.github.io/raw/master/btc.png
    :alt: Bitcoin donation
    :target: https://m.freewallet.org/id/374ad82e/btc
.. image:: https://github.com/jaymoulin/jaymoulin.github.io/raw/master/ltc.png
    :alt: Litecoin donation
    :target: https://m.freewallet.org/id/374ad82e/ltc
.. image:: https://github.com/jaymoulin/jaymoulin.github.io/raw/master/utip.png
    :alt: Watch Ads
    :target: https://utip.io/femtopixel
.. image:: https://github.com/jaymoulin/jaymoulin.github.io/raw/master/ppl.png
    :alt: PayPal donation
    :target: https://www.paypal.me/jaymoulin
.. image:: https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png
    :alt: Buy me a coffee
    :target: https://www.buymeacoffee.com/3Yu8ajd7W


This program will allow you to be notified of Github new releases

Installation
------------

.. code::

    pip3 install github-release-notifier

Usage
-----

.. code::

    usage: github-release-notifier [-h] [--action {cron,subscribe,unsubscribe}] [--package PACKAGE]
                  [--webhook WEBHOOK] [--uuid UUID]

    optional arguments:
      -h, --help            show this help message and exit
      --action {cron,subscribe,unsubscribe}, -a {cron,subscribe,unsubscribe}
                            Action to do (default: cron)
      --package PACKAGE, -p PACKAGE
                            Github package name / url (required for
                            subscribe/unsubscribe) - prints uuid on subscription
      --webhook WEBHOOK, -w WEBHOOK
                            URL to your webhook (required for
                            subscribe/unsubscribe)
      --uuid UUID, -u UUID  UUID of your webhook (required for unsubscribe)

Example
~~~~~~~

First, I register my webhook :

.. code::

    github-release-notifier --action subscribe --webhook https://example.com/updated --package jaymoulin/google-music-manager

an UUID is printed. this UUID will be required to unsubscribe the webhook.

When `jaymoulin/google-music-manager` releases a new version, `https://example.com/updated` will be called with HTTP method `POST` and body, a JSON like this :

.. code::

    {
        "date": [2017, 11, 13, 19, 46, 35, 0, 317, 0],
        "version": "0.7.2",
        "title": "Fixes split modules",
        "content": "",
        "media": "https://avatars0.githubusercontent.com/u/14236493?s=60&v=4",
        "author": "jaymoulin"
        "package_name": "jaymoulin/google-music-manager"
    }

For this to happen, the system should check if a new version have been released.
We can do that by calling `github-release-notifier` without any parameter or setting `--action` to `cron` (which is default).

To automate this process, we could add this process in a cronjob:

.. code::

    (crontab -l ; echo "0 0 * * * github-release-notifier") | sort - | uniq - | crontab -

This will check every day at midnight if new versions have been released.

Configuration
-------------

Environment variables can be defined to change default `hooks` or `versions` database files (plain json file)

.. code::

    GRN_VERSIONS_FILE: Path to saved versions (default: ${HOME}/.github_release_notifier/versions)
    GRN_HOOKS_FILE: Path to hooks configuration (default: ${HOME}/.github_release_notifier/hooks)

Docker Usage
------------

First run the daemon

.. code::

    docker run --name GRN -d femtopixel/github-release-notifier

you can mount a volume to `/root/.github_release_notifier/` to keep tracks of webhooks and versions

example:

.. code::

    docker run --name GRN -d -v /path/to/your/saves:/root/.github_release_notifier/ femtopixel/github-release-notifier

Then register your webhook :

.. code::

    docker exec GRN -a subscribe -p jaymoulin/google-music-manager -w https://example.com/updated


Submitting bugs and feature requests
------------------------------------

Bugs and feature request are tracked on GitHub

Author
------

Jay MOULIN jaymoulin+github-release-notifier@gmail.com See also the list of contributors which participated in this program.

License
-------

Github Release Notifier is licensed under the MIT License
