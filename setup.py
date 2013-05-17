try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Agenda cultural de Córdoba',
    'author': 'Carlos de la Torre',
    'url': 'http://www.carlosmatias.com.ar/.',
    'download_url': 'Where to download it.',
    'author_email': 'cmdelatorre@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['agendacultural'],
    'scripts': [],
    'name': 'agendacultural'
}

setup(**config)