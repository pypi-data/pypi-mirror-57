try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import os

this_directory = os.path.abspath(os.path.dirname(__file__))

# get __version__ from _version.py
ver_file = os.path.join('transfertools', 'version.py')
with open(ver_file) as f:
    exec(f.read())

# read the contents of README.md
def readme():
    with open(os.path.join(this_directory, 'README.md')) as f:
        return f.read()

# read the contents of requirements.txt
with open(os.path.join(this_directory, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

# setup configuration
config = {
    'name': 'transfertools',
    'version': __version__,
    'description':'A compact Python toolbox for transfer learning.',
    'long_description': readme(),
    'long_description_content_type': 'text/markdown',
    'url': 'https://github.com/Vincent-Vercruyssen/transfertools',
    'author': 'Vincent Vercruyssen',
    'author_email': 'V.Vercruyssen@gmail.com',
    'keywords': [
        'transfer learning',
        'anomaly detection',
        'domain adaptation',
        'instance weighting'
    ],
    'install_requires': requirements,
    'packages': find_packages(exclude=['test']),
    'package_dir' : {'transfertools': 'transfertools'},
    'include_package_data': True,
    'include_package_data': True,
    'classifiers':[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3'
    ]
}

setup(**config)