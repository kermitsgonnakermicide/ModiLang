from setuptools import setup, find_packages

setup(
    name='modilang',
    version='0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'modilang = modilang.cli:main'
        ]
    },
)
