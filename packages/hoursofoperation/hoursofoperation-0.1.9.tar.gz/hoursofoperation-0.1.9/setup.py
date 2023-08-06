from setuptools import setup, find_packages


_version = {}
exec(open('hoursofoperation/_version.py').read(), _version)


config = dict(
    name='hoursofoperation',
    packages=find_packages('.', include=['hoursofoperation.*']),
    version=_version['__version__'],
    description = 'Utilities for loading and doing calculations with a partner\'s hours of operations configration.',
    author='Ashley Fisher',
    author_email='fish.ash@gmail.com',
    url='https://github.com/Brightmd/hoursofoperation',
    keywords=['hours'],
    classifiers=[],
    scripts=[],
    install_requires=[
        'codado',
        'python-dateutil',
        'pytz',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-coverage',
            'pytest-flakes',
            'tox',
    ]},
)


setup(**config)
