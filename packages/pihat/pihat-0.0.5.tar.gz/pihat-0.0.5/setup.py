#!/usr/bin/env python3

"""Setup script"""

from setuptools import setup, find_packages

setup(
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
        "GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Boot",
        "Topic :: System :: Hardware :: Hardware Drivers",
    ],
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    use_scm_version=True,
    python_requires='>=3.7',
    setup_requires=[
        'setuptools_scm',
    ],
    install_requires=[
        'fdt',
        'pyyaml',
        'schema',
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'pihat-eeprom=pihat.eeprom.cli:main',
        ],
    },
)
