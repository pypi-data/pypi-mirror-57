# -*- coding: utf-8 -*-
from setuptools import setup
import allianceauth

install_requires = [
    'mysqlclient',
    'dnspython',
    'passlib',
    'requests>=2.9.1',
    'bcrypt',
    'python-slugify>=1.2',
    'requests-oauthlib',
    'semantic_version',

    'redis<=2.10.6',
    'celery>=4.0.2,<4.3.0',
    'celery_once',

    'django>=2.0,<3.0',
    'django-bootstrap-form',
    'django-registration==2.4',
    'django-sortedm2m',
    'django-redis-cache==1.8.1',
    'django-celery-beat<=1.1.1',

    'openfire-restapi',
    'sleekxmpp',

    'adarnauth-esi>=1.4.10,<2.0',
    'kombu<=4.3.0',
]

testing_extras = [
    'coverage>=4.3.1',
    'requests-mock>=1.2.0',
    'django-nose',
    'django-webtest',
]

setup(
    name='allianceauth',
    version=allianceauth.__version__,
    author='Alliance Auth',
    author_email='adarnof@gmail.com',
    description='An auth system for EVE Online to help in-game organizations manage online service access.',
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        ':python_version=="3.4"': ['typing'],
    },
    python_requires='~=3.4',
    license='GPLv2',
    packages=['allianceauth'],
    url='https://gitlab.com/allianceauth/allianceauth',
    zip_safe=False,
    include_package_data=True,
    entry_points="""
            [console_scripts]
            allianceauth=allianceauth.bin.allianceauth:main
    """,
)
