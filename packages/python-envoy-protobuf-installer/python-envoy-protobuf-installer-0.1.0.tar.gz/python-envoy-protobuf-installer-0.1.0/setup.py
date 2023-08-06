#!/usr/bin/env python

"""The setup script."""

from setuptools import (
    find_packages,
    setup,
)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def get_requirements(env=None):
    if env:
        env = f'-{env}'
    with open(f'requirements{env if env else ""}.txt') as fp:
        return [
            line.strip()
            for line in fp.readlines()
            if not line.startswith('#')
        ]


setup(
    author="Derrick Petzold",
    author_email='github@petzold.io',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description="Installer for Envoy Protobuf files",
    entry_points={
        'console_scripts': [
            'envoy-protobuf-builder=envoy_protobuf.main:main',
        ],
    },
    extras_require={
        'dev': get_requirements('dev') + get_requirements('test'),
    },
    install_requires=get_requirements(),
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='envoy_protobuf',
    name='python-envoy-protobuf-installer',
    packages=find_packages(
        include=[
            'envoy_protobuf',
            'envoy_protobuf.*'
        ]
    ),
    setup_requires=get_requirements('setup'),
    test_suite='tests',
    tests_require=get_requirements('test'),
    url='https://github.com/dpetzold/envoy_protobuf',
    version='0.1.0',
    zip_safe=False,
)
