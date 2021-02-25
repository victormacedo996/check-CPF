
from setuptools import setup

setup(
    name = 'check-CPF',
    version = 'v0.1.0',
    author = 'Victor Macedo',
    author_email = 'victormacedo996@gmail.com',
    packages = ['check-CPF'],
    description = 'Tool to verify if the inputed CPF is a valid CPF or not. It returns a eleven digit interger number',
    long_description = 'It returns a eleven digit interger number. ',
    url = 'https://github.com/victormacedo996/check-CPF',
    project_urls = {
        'Código fonte': 'https://github.com/victormacedo996/check-CPF',
        'Download': 'https://github.com/yanorestes/aluratemp/archive/1.0.0.zip'
    },
    license = 'MIT',
    keywords = 'CPF' 'validate' 'validar' 'cadastro de pessoa física',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English (US)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization'
    ]
)