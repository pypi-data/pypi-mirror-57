import setuptools
from shawnguo.version import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'shawnguo',
    packages = ['shawnguo'],
    version = version,  # Ideally should be same as your GitHub release tag version
    description = 'Shawn Guo\'s project',
    long_description = long_description,
    long_description_content_type="text/markdown",
    author = 'Shawn Guo',
    author_email = 'shawnguo.cn@gmail.com',
    url = 'https://github.com/Shawn-Guo-CN/shawnguo',
    keywords = ['shawnguo', 'python'],
    classifiers = [
        'Programming Language :: Python :: 3.6',
    ],
)