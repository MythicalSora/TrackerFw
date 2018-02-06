from setuptools import setup, find_packages
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='trackerfw',
    version='0.0.1',
    description='TrackerFw - firewall for trackers',
    long_description=long_description,
    url='https://github.com/PrivacySec/TrackerFw',
    author='Dillen Meijboom',
    author_email='info@dmeijboom.nl',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='trackerfw tracker-fw anti-track ghostery',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.5',

    install_requires=[
        'PyYAML',
        'Jinja2',
        'aiohttp',
        'aiohttp-jinja2'
    ],

    entry_points={
        'console_scripts': [
            'trackerfw=trackerfw:main',
        ],
    },
)