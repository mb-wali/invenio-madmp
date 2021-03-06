# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Sotiris Tsepelakis.
#
# invenio-maDMP is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio modules that handles maDMPs"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.3.3',
    'pydocstyle>=2.0.0',
    'pytest-cov>=2.5.1',
    'pytest-pep8>=1.0.6',
    'pytest-invenio>=1.0.5',
]

extras_require = {
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'Babel>=1.3',
    'pytest-runner>=3.0.0,<5',
]

install_requires = [
    'elasticsearch>=6',
    'elasticsearch_dsl',
    'Flask-BabelEx>=0.9.3',
    'flask-login>=0.3.2,<0.5',
    'flask-security',
    'invenio-db',
    'invenio-files-rest',
    'invenio-indexer',
    'invenio-pidstore',
    'invenio-records',
    'invenio-records-files',
    'invenio-search',
    'werkzeug>=0.14.1',
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_madmp', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-madmp',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio maDMP',
    license='MIT',
    author='Sotiris Tsepelakis',
    author_email='leizersotos@gmail.com',
    url='https://github.com/inveniosoftware/invenio-madmp',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.apps': [
            'invenio_madmp = invenio_madmp:inveniomaDMP',
        ],
        'invenio_base.blueprints': [
            'invenio_madmp = invenio_madmp.views:blueprint',
        ],
        'invenio_i18n.translations': [
            'messages = invenio_madmp',
        ],
        # 'invenio_access.actions': [],
        # 'invenio_admin.actions': [],
        # 'invenio_assets.bundles': [],
        # 'invenio_base.api_apps': [],
        'invenio_base.api_blueprints': [
            'invenio_madmp = invenio_madmp.api:blueprint'
        ],
        # 'invenio_celery.tasks': [],
        # 'invenio_db.models': [],
        # 'invenio_pidstore.minters': [],
        # 'invenio_records.jsonresolver': [],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 2 - Pre-Alpha',
    ],
)
