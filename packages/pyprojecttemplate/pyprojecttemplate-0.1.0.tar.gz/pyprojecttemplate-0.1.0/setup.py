from os.path import dirname, join, abspath
from setuptools import setup, find_packages

here = abspath(dirname(__file__))

# Get the long description from the README file
with open(join(here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()

install_requires = [
    # List project dependencies here
    'requests'
]

setup(
    name='pyprojecttemplate',
    version="0.1.0",
    description="Example Project Structure for a Python / PyPI Project",
    long_description=README,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='project template python',
    author='Patrick Shiel',
    author_email='patrick.shiel.io@gmail.com',
    url='https://github.com/patrickshiel/python-package-template',
    license='MIT',
    packages=find_packages(exclude=('tests', 'tests.*')),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires
)
