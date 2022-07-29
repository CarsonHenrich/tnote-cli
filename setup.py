from setuptools import setup
setup(
    name = 'tnote-cli',
    version = '0.1.0',
    packages = ['tnote'],
    entry_points = {
        'console_scripts': [
            'tn = tnote.__main__:main'
        ]
    })
