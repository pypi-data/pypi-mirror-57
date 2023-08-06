import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION_MAJOR = '0'
VERSION_MINOR = '0'
VERSION_PATCH = '2'


def version_number():
    return '{}.{}.{}'.format(VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)


setuptools.setup(
    name="tello_edu_py",
    version=version_number(),
    author="Tariq86",
    author_email="tariq.86@pm.me",
    description="Full-Featured Python SDK for Tello EDU",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tariq86/tello_edu.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
