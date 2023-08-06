import codecs
import os
import re

from setuptools import setup, find_packages


HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):  # Stolen from txacme
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('seed_control_interface_service')


setup(
    name="seed-control-interface-service",
    version=version,
    url='http://github.com/praekelt/seed-control-interface-service',
    license='BSD',
    description='Seed Control Interface Service',
    long_description=read('README.rst'),
    author='Praekelt.org',
    author_email='dev@praekelt.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django==2.2.8',
        'djangorestframework==3.9.1',
        'coreapi==2.3.3',
        'dj-database-url==0.3.0',
        'psycopg2==2.7.1',
        'raven==6.10.0',
        'django-filter==2.2.0',
        'whitenoise==2.0.6',
        'celery==3.1.24',
        'django-celery==3.3.0',
        'redis==2.10.5',
        'pytz==2015.7',
        'django-rest-hooks==1.5.0',
        'seed-services-client==0.31.0',
        'six==1.10.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
