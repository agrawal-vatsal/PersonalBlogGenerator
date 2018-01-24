from setuptools import setup

setup(
    name='generate',
    version='1.0',
    py_modules=['generate'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        generate=generate:cli
    ''',
)
