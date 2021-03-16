from io import open

from setuptools import find_packages, setup

with open('forskalle_api/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = ['click', 'requests', 'PyYAML', 'click_log']

setup(
    name='forskalle-api',
    version=version,
    description='Library for Fsk3 API',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Heinz Axelsson-Ekker',
    author_email='heinz.ekker@vbcf.ac.at',
    maintainer='Heinz Axelsson-Ekker',
    maintainer_email='heinz.ekker@vbcf.ac.at',
    url='https://ngs.vbcf.ac.at/repo/software/forskalle-api',

    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
    entry_points={
        'console_scripts': {
            'fsk-cli = forskalle_api.cli:cli',
        }
    }
)
