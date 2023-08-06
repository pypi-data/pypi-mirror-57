from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ehelply-logger',
    packages=find_packages(),
    version='0.0.8',
    description='Logger.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shawn Clake',
    author_email='shawn.clake@gmail.com',
    url='https://github.com/ehelply/Logger',
    keywords=['logger'],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'pytest'
    ],
)
