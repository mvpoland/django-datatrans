#!/usr/bin/env python
from setuptools import (setup, find_packages)
import datatrans

LONG_DESCRIPTION = """

"""


setup(
    name='django-datatrans',
    version=datatrans.__version__,
    description='Translate Django models without changing anything to existing applications and their '
              'underlying database.',
    long_description=LONG_DESCRIPTION,
    author='Jef Geskens, VikingCo nv',
    author_email='jef.geskens@mobilevikings.com',
    url='http://github.com/citylive/django-datatrans/',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Topic :: Software Development :: Internationalization',
    ],
    python_require=">=3.5"
)
