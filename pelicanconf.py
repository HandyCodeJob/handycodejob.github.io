#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Handy Code Job, LLC'
SITENAME = 'Handy Code Job'
SITEURL = 'handycodejob.com'

PATH = 'content'

TIMEZONE = 'America/Boise'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget

SOCIAL = (('Github', 'https://github.com/handycodejob'),
          ('YouTube', 'https://www.youtube.com'),
          ('Bitbucket', 'https://bitbucket.com/handycodejob'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# Style Stuff
THEME = 'materialistic-pelican'
USE_CDN = True
USER_LOGO_URL = SITEURL + "static/images/logo.svg" #: an image around 100px square
#SITETAGLINE = "Mike & Zoey's life style blog" #: a short sentence that describes your site
#SITEDESCR = "Mike & Zoey live in Boise, ID together. They love good food and happy hour!" #: a longer description of your site
GITHUB_URL = "https://github.com/mikemhenry" #: URL to your GitHub page, for the social icons
#LINKEDIN_URL #: URL to your LinkedIn page, for the social icons
TWITTER_URL = "https://twitter.com/ZoeyHogue" #: URL to your Twitter page, for the social icons
#FACEBOOK_URL#: URL to your Facebook page, for the social icons
#GOOGLE_URL#: URL to your Google Plus page, for the social icons
#FLICKR_URL#: URL to your Flickrpage, for the social icons
LICENSE_NAME = "CC BY-NC-SA"#: the license for your content (e.g. CC BY-SA)
LICENSE_URL = "http://creativecommons.org/licenses/by-nc-sa/4.0/" #: the link to where the full text of your license is
ARCHIVES_URL = "archives.html" #: the link to your archives
#CONTACT_URL#: the link to your contact page
PRIMARY_COLOR = 'Cyan'
ACCENT_COLOR = 'Blue'
STATIC_PATHS = ['static']
