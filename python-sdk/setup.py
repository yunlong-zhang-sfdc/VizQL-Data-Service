"""
Setup configuration for the VizDataService Python Client.
"""

from setuptools import setup, find_packages
import os
import requests
import json
from typing import Optional, Dict, Any

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "vizqldataservicesdk"
PYTHON_REQUIRES = ">= 3.8"

def read_version() -> str:
    """
    Read the version from the OpenAPI schema.
    
    Returns:
        str: The version number or 'UNKNOWN' if not found
    """
    url = 'https://raw.githubusercontent.com/tableau/VizQL-Data-Service/refs/heads/main/VizQLDataServiceOpenAPISchema.json'
    read_file = read_json_from_url(url)
    if read_file is not None:
        return read_file['info']['version']
    return 'UNKNOWN'

def read_json_from_url(url: str) -> Optional[Dict[str, Any]]:
    """
    Read JSON data from a URL.
    
    Args:
        url: The URL to read from
        
    Returns:
        Optional[Dict[str, Any]]: The JSON data or None if failed
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return None

def package_files(directory: str) -> list:
    """
    Get a list of files in a directory for package data.
    
    Args:
        directory: The directory to scan
        
    Returns:
        list: List of file paths
    """
    paths = []
    for (path,directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

# Get example files
extra_files = package_files('examples/payloads')

setup(
    name=NAME,
    version=read_version(),
    description="A Python client library for interacting with the VizDataService API",
    long_description_content_type="text/markdown",
    author="Tableau",
long_description="""\
    python sdk to query Tableau published data sources
    """,
    author_email="ajonnavittula@tableau.com",
    url="",
    project_urls={
        "Bug Tracker": "",
        "Documentation": "",
        "Source Code": "",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    test_requires=["pytest"],
    python_requires=PYTHON_REQUIRES,
    install_requires=[
        "certifi>=2025.1.31",
        "charset-normalizer>=3.4.1",
        "defusedxml>=0.7.1",
        "distlib>=0.3.6",
        "filelock>=3.10.7",
        "future>=0.17.1",
        "idna>=3.10",
        "packaging>=24.2",
        "platformdirs>=2.6.2",
        "requests>=2.32.3",
        "setuptools>=58.4.0",
        "six>=1.16.0",
        "tableauserverclient>=0.36",
        "virtualenv>=20.15.1",
        "wheel>=0.37.0",
        "python-dateutil>=2.8.2",
        "httpx>=0.23.3",
        "urllib3>=1.25.3,<3.0.0",
        "pydantic>=2.0.0",
        "typing-extensions>=4.7.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    package_data={
        "vizqldataservicesdk": ['examples/payloads/*.json']
    },
    include_package_data=True,
)