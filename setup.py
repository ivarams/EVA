#!/usr/bin/env python3

config = {
    'description': 'Event Adapter',
    'author': 'MET Norway',
    'url': 'https://github.com/metno/productstatus-eva',
    'download_url': 'https://github.com/metno/productstatus-eva',
    'author_email': 'it-geo-tf@met.no',
    'version': '1.0',
    'install_requires': [
        'nose==1.3.7',
        'python-dateutil==2.5.0',
        'productstatus-client==6.2.0',
        'paramiko==1.16.0',
        'mock==1.3.0',
        'httmock==1.2.4',
        'jinja2==2.8',
        'kazoo==2.2.1',
    ],
    'packages': [],
    'scripts': [],
    'name': 'eva'
}

if __name__ == '__main__':
    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    setup(**config)
