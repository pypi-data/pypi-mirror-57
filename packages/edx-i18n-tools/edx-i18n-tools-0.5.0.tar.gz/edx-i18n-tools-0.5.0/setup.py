#!/usr/bin/env python

from setuptools import setup

setup(
    name='edx-i18n-tools',
    version='0.5.0',
    description='edX Internationalization Tools',
    author='edX',
    author_email='oscm@edx.org',
    url='https://github.com/edx/i18n-tools',
    packages=[
        'i18n',
    ],
    install_requires=[
        'django>=1.11,<2.3',
        'polib',
        'path.py>=7.0',
        'pyYaml',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'i18n_tool = i18n.main:main',
        ],
    },
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
    ],
)
