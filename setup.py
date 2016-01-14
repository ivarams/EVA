try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Event Adapter',
    'author': 'MET Norway',
    'url': 'https://github.com/metno/productstatus-eva',
    'download_url': 'https://github.com/metno/productstatus-eva',
    'author_email': 'it-geo-tf@met.no',
    'version': '0.1',
    'install_requires': [
        'nose==1.3.7',
        'python-dateutil==2.4.2',
        'productstatus-client==3.1.2',
    ],
    'packages': [],
    'scripts': [],
    'name': 'eva'
}

setup(**config)
