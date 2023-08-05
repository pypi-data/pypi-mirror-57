#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.install import install

import subprocess
import sys


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()


common_requirements = [
    'Click>=7.0',
    'tensorflow-hub',
    'pillow',
    'pycocotools',
    'jupyter',
    'h5py',
]

trainer_requirements = [
    'tensorflow==2.0.0',
    'numpy'
]

trainer_requirements = list(map(
    lambda x: x + ';platform_machine=="x86_64"', trainer_requirements
))

rpi_requirements = [
    'smbus',
    'picamera',
    'pantilthat>=0.0.7',
    'tensorflow@https://github.com/leigh-johnson/Tensorflow-bin/blob/master/tensorflow-2.0.0-cp37-cp37m-linux_armv7l.whl?raw=true'
]

rpi_requirements = list(map(
    lambda x: x + ';platform_machine=="armv7l"', rpi_requirements))

requirements = common_requirements + trainer_requirements + rpi_requirements

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

RPI_LIBS = ['python3-dev', 'cmake', 'libjpeg8-dev', 'zlib1g-dev']
RPI_CUSTOM_COMMANDS = [['sudo', 'apt-get', 'update'],
                       ['sudo', 'apt-get', 'install', '-y'] + RPI_LIBS
                       ]

TRAINER_DEBIAN_LIBS = ['python3-dev', 'cmake', 'zlib1g-dev', 'libjpeg-dev']

TRAINER_DEBIAN_CUSTOM_COMMANDS = [['apt-get', 'update'],
                                  ['apt-get', 'install', '-y'] + TRAINER_DEBIAN_LIBS]

TRAINER_DARWIN_LIBS = ['cmake']
TRAINER_DARWIN_CUSTOM_COMMANDS = [['brew', 'update'],
                                  ['brew', 'install'] + TRAINER_DARWIN_LIBS
                                  ]


# $pip install rpi-deep-pantilt==1.0.0rc3
# Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
# Collecting rpi-deep-pantilt==1.0.0rc3
#   Using cached https://files.pythonhosted.org/packages/91/d0/aba792a5fc8d50b8e7fcbd24ceb438d106cc9eb294760211468bf3400f6f/rpi_deep_pantilt-1.0.0rc3.tar.gz
# ERROR: Packages installed from PyPI cannot depend on packages which are not also hosted on PyPI.
# rpi-deep-pantilt depends on object-detection@ git+https://github.com/leigh-johnson/models@tf-compat-patch#egg=object_detection&subdirectory=research
class PostInstall(install):
    git_eggs = ' git+https://github.com/leigh-johnson/models@tf-compat-patch#egg=object_detection&subdirectory=research'

    def run(self):
        install.run(self)
        # https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program
        subprocess.call([sys.executable, '-m', 'pip',
                         'install', self.git_eggs])


class BuildCommand(build_py):
    '''Extend setuptools build to deserialize protos on build.'''

    def run(self):
        cmd = ['make', 'protoc']
        p = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        stdout, stderr = p.communicate()
        print(f'Command output: {stdout}')
        if p.returncode != 0:
            raise RuntimeError(
                f'{cmd} failed: exit code: {p.returncode} \n {stderr}')
        build_py.run(self)


setup(
    author="Leigh Johnson",
    author_email='hi@leighjohnson.me',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An example of deep object detection and tracking with a Raspberry Pi, PiCamera, and Pimoroni Pantilt Hat",
    entry_points={
        'console_scripts': [
            'rpi-deep-pantilt=rpi_deep_pantilt.cli:main',
        ],
    },
    # cmdclass={'build_py': BuildCommand, 'install': PostInstall},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='computer vision cv tensorflow raspberrypi detection tracking ',
    name='rpi_deep_pantilt',
    packages=find_packages(include=[
                           'rpi_deep_pantilt', 'rpi_deep_pantilt.*', 'models', 'models.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/leigh-johnson/rpi_deep_pantilt',
    version='1.0.0rc4',
    zip_safe=False,

)
