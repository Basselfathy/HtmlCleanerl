from setuptools import setup, find_packages

setup(
    name="html_cleaner",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "lxml",
        "rich",
        "httpx",
    ],
    description="A Python library to clean HTML text nodes by keeping only the first word.",
    author="Bassel Fathy",
    author_email="basselfathy@gmail.com",
    url="https://github.com/Basselfathy/html_cleaner",
)