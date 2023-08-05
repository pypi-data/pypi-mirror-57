from setuptools import setup


version = "3.1.0"
author = "jieggii"
description = "String generator based on Markov process"

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="mc.py",
    license="MIT",
    python_requires=">=3",
    version=version,
    author=author,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jieggii/mc.py",
    author_email="jieggii@protonmail.com",
    packages=["mc"],
    project_urls={
        "Documentation": "https://github.com/jieggii/mc.py/blob/master/docs/README.md",
        "Source": "https://github.com/jieggii/mc.py",
        "Tracker": "https://github.com/jieggii/mc.py/issues",
    },
)
