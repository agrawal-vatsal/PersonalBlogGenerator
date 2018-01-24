from setuptools import setup

setup(
    name='gen',
    version='1.0',
    py_modules=['gen'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gen=gen:cli
    ''',
)
