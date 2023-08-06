import codecs
import os
import re

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):  # Stolen from txacme
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version("seed_stage_based_messaging")


setup(
    name="seed-stage-based-messaging",
    version=version,
    url="http://github.com/praekelt/seed-stage-based-messaging",
    license="BSD",
    description="Seed Stage Based Messaging microservice",
    long_description=read("README.rst"),
    author="Praekelt.org",
    author_email="dev@praekelt.org",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django==2.2.8",
        "djangorestframework==3.9.1",
        "coreapi==2.3.3",
        "dj-database-url==0.5.0",
        "psycopg2==2.7.5",
        "raven==6.9.0",
        "django-filter==2.0.0",
        "celery==4.2.1",
        "pytz==2018.5",
        "requests==2.20.0",
        "seed-services-client==0.37.2",
        "croniter==0.3.25",
        "sftpclone==1.2.2",
        "django-prometheus==1.0.15",
        "django-environ==0.4.5",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
