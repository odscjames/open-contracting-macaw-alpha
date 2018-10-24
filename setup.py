from setuptools import setup, find_packages

setup(
    name='ocdsmacaw',
    version='0.0.0',
    author='Open Contracting Partnership',
    author_email='data@open-contracting.org',
    url='https://github.com/xxxxxxxxxxxxx/xxxxxx',
    description='A data review library',
    license='BSD',
    packages=find_packages(),
    long_description='A data review library',
    install_requires=[
        'jsonref',
        'jsonschema',
    ],
)

