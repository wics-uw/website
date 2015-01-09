#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'WiCS Undergraduate Committee'
SITENAME = u'Women in Computer Science'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = [ 'images', 'extra' ]
EXTRA_PATH_METADATA = {
    'extra/robots.txt':   # sit these in the top directory
        {'path': 'robots.txt'},
    'extra/favicon.ico':
        {'path': 'favicon.ico'},
}

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

TIMEZONE = 'Canada/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Women in Computer Science Committee', 
          'https://cs.uwaterloo.ca/wics'),
         ('Women in Engineering', 'https://uwaterloo.ca/women-in-engineering/'),
         ('Women Who Code Waterloo',
          'http://www.meetup.com/Women-Who-Code-Waterloo/'),
         ('Women in STEM (WiSTEM)', 'http://uwwistem.weebly.com/'),
         ('FemPhys', 'https://www.facebook.com/groups/705741329511034/'),
         ('Geek Feminism Wiki', 'http://geekfeminism.wikia.com/'),
         ('The Ada Initiative', 'http://adainitiative.org/'),
         ('WiCS IRC Web Chat', 'http://webchat.oftc.net/?channels=wics'),
        )

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/groups/wicsUW'),
          ('Twitter', 'https://twitter.com/wicsuw'),
          ('GitHub', 'https://github.com/wics-uw'),
         )
TWITTER_USERNAME = 'wicsuw'

DEFAULT_PAGINATION = 5

THEME = 'themes/notmyidea'
