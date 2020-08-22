import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="pybites-tips",
    version="1.0.0",
    description="Read PyBites Python tips from the command line",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/PyBites-Open-Source/pybites-tips",
    author="PyBites",
    author_email="support@pybit.es",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pytip"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "pytip=pytip.__main__:main",
        ]
    },
)
