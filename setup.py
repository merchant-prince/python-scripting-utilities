import setuptools


with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name = "harivansh-scripting-utilities",
    version = "0.1.0",
    author = "Harivansh",
    author_email = "hello@harivan.sh",
    description = "Some utilities to facilitate writing python scripts.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/merchant-prince/python-scripting-utilities",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX"
    ],
    python_requires = '>=3.8',
)
