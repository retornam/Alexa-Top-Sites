from setuptools import setup

setup(name  = 'alexa-top-sites',
version     = '0.2',
packages    = ['alexa'],
install_requires=['beautifulsoup4','requests', 'coverage', 'lxml'],
url = 'http://github.com/davedash/Alexa-Top-Sites',
author = 'Dave Dash',
author_email = 'dd+github@davedash.com',
)
