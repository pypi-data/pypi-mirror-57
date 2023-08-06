"""
Sesh is a tool for managing music classes from the command line.
Copyright (C) 2019  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

from sesh.config.base_config import SESH_DB_PATH
from sesh.init_db import _init_db
from sesh.__version__ import __version__, _version_min_python_


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    def run(self):
        develop.run(self)
        if not SESH_DB_PATH.exists():
            _init_db()


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        if not SESH_DB_PATH.exists():
            _init_db()


with open("README.rst", "r") as fh:
    long_description = fh.read()

required = [
]

setup(
    name='sesh',
    version=__version__,
    python_requires=f">={_version_min_python_}",
    install_requires=required,

    packages=find_packages(),
    package_data={
        'sesh': ['config/*.json', 'config/*.py'],
    },
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand
    },
    license='AGPLv3',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "License :: OSI Approved :: "
        "GNU Affero General Public License v3 or later (AGPLv3+)",
        "Topic :: Education",
        "Topic :: Office/Business :: Scheduling",
        "Environment :: Console",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],

    url='https://pypi.org/project/sesh/',
    author="Brian Farrell",
    author_email="brian.farrell@me.com",
    description="A tool for managing music classes from the command line.",
    long_description=long_description,
    long_description_content_type='text/x-rst',
    keywords="interface",
    entry_points={
        "console_scripts": [
            "sesh=sesh:main",
        ],
    },
    zip_safe=False,
)
