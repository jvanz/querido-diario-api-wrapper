# coding: utf-8

"""
    Querido Diário

    API to access the gazettes from all Brazilian cities  # noqa: E501

    The version of the OpenAPI document: 0.17.0
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "querido-diario"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.7.0",
    "setuptools >= 21.0.0",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.7",
]

setup(
    name=NAME,
    version=VERSION,
    description="Querido Diário",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Querido Diário"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    API to access the gazettes from all Brazilian cities  # noqa: E501
    """
)
