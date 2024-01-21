from setuptools import setup, find_packages

setup(
    name='Onet',
    version='1.0.1',
    description='Onet_Web_Scraping',
    author='Peter_Cheng',
    packages=find_packages(),
    install_requires=['requests', 'pandas', 'bs4'],
)