from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="harivansh-scripting-utilities",
    version="0.4.1",
    description="Some utilities to facilitate writing python scripts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/merchant-prince/python-scripting-utilities",
    author="Harivansh",
    author_email="hello@harivan.sh",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX"
    ],
    keywords="python scripting utilities",
    packages=["harivansh_scripting_utilities"],
    python_requires=">=3",
    install_requires=[
        "termcolor"
    ]
)
