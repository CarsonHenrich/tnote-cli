from setuptools import setup
setup(
    name='tnote-cli',
    version='0.1.0',
    packages=['tnote'],
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts': [
            'tn = tnote.__main__:main'
        ]
    }
)
from pathlib import Path
from setuptools import find_packages, setup
dependencies = []
# read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()
setup(
    name='tnote-cli',
    packages=find_packages(),
    version='0.0.1',
    description='A simple Terminal-based notes app',
    author='Carson Henrich',
    author_email='contact@carsonhenrich.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='',
    project_urls={
        '': 'https://github.com/',
    },
    classifiers=[
        'Programming Language :: Python :: VERSION',
        'License ::  :: ',
        'Operating System :: ',
    ]
    install_requires=dependencies,
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    )
