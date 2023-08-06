import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="urlshortener",
    version="1.0.0",
    description="shorten long urls",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/3ep-one/urlshortener",
    author="Sepehr Rafiei",
    author_email="sepehr.rafiei.k@ut.ac.ir",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["urlshortener"],
    include_package_data=True,
    install_requires=["redis", "HTTPServer"],
    entry_points={
        "console_scripts": [
            "urlshortener=urlshortener.__main__:main",
        ]
    },
)
