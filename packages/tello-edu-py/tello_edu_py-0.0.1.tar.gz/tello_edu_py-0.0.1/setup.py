import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tello_edu_py",
    version="0.0.1",
    author="Tariq86",
    author_email="tariq.86@pm.me",
    description="Full Python SDK for Tello EDU",
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
