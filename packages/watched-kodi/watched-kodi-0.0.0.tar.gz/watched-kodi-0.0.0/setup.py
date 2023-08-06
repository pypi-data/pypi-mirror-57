import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as f:
    README = f.read()

setup(
    name="watched-kodi",
    version="0.0.0",
    description="WATCHED.com Kodi SDK",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/watchedcom/sdk-kodi",
    author="WATCHED",
    author_email="dev@watched.com",
    packages=find_packages(),
    install_requires=["watched-sdk"],
    python_requires=">=3.4",
)
