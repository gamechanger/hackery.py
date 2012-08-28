import os
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name="Hackery",
    version="0.0.7",
    author="Kiril Savino",
    author_email="kiril@gamechanger.io",
    description="hack labeling and tracking library",
    license="BSD",
    keywords="hack",
    url="http://github.com/gamechanger/hackery.py",
    packages=["hackery"],
    long_description=read("README"),
    )
