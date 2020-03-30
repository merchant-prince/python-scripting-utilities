import setuptools


with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="merchant-prince-scripting-utilities",
    version="0.0.1",
    author="Harivansh",
    author_email="hello@harivan.sh",
    description="Some utilities to facilitate writing python scripts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPL v3.0",
        "Operating System :: POSIX"
    ],
    python_requires='>=3.8',
)