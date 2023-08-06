from io import open

from setuptools import find_packages, setup

with open('autobots/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = []

setup(
    name='autobots',
    version=version,
    description='transformers based nlp library',
    long_description=readme,
    author='maxentlabs.ai team',
    author_email='royalkingpin@gmail.com',
    maintainer='maxentlabs.ai',
    maintainer_email='royalkingpin@gmail.com',
    url='https://github.com/maxent-ai/autobots',
    license='MIT',

    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
)
