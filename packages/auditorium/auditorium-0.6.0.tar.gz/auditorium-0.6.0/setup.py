# coding: utf8

import toml
from setuptools import setup


# TODO: Update version whenever changes
VERSION = '0.6.0'


def get_install_requirements():
    """Automatically pull requirements from Pipfile.
    Adapted from: <https://medium.com/homeaway-tech-blog/simplifying-python-builds-74e76802444f>
    """
    try:
        # read my pipfile
        with open ('Pipfile', 'r') as fh:
            pipfile = fh.read()
        # parse the toml
        pipfile_toml = toml.loads(pipfile)
    except FileNotFoundError:
        return []
    # if the package's key isn't there then just return an empty
    # list
    try:
        required_packages = pipfile_toml['packages'].items()
    except KeyError:
        return []
    # If a version/range is specified in the Pipfile honor it
    # otherwise just list the package
    return ["{0}{1}".format(pkg,ver) if ver != "*"
            else pkg for pkg,ver in required_packages]


setup(
    # TODO: Change your library name and additional information down here
    name='auditorium',
    packages=['auditorium'],
    url='https://github.com/apiad/auditorium',
    download_url='https://github.com/apiad/auditorium/tarball/{}'.format(VERSION),
    license='MIT',
    author='Alejandro Piad',
    author_email='apiad@apiad.net',
    description='A Python-powered slideshow maker with steroids.',
    include_package_data=True,
    zip_safe=False,

    # This should automatically take your long description from Readme.md
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    # This should automatically pull your requirements from `Pipfile`
    install_requires=get_install_requirements(),
    version=VERSION,

    # TODO (Optional): Set your entry-points (CLI apps to register) here
    entry_points={
        'console_scripts': ['auditorium=auditorium.__main__:main'],
    },

    # TODO: Choose your classifiers carefully
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
