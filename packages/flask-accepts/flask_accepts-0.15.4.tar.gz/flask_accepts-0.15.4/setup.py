# Copyright Alan (AJ) Pryor, Jr. 2018

from setuptools import setup, find_packages

setup(
    name="flask_accepts",
    author='Alan "AJ" Pryor, Jr.',
    author_email="apryor6@gmail.com",
    version="0.15.4",
    description="Easy, opinionated Flask input/output handling with Flask-RESTplus and Marshmallow",
    ext_modules=[],
    packages=find_packages(),
    install_requires=[
        "marshmallow>=3.0.1",
        "flask-restplus>=0.12.1",
    ],
)
