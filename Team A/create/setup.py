from setuptools import setup

setup(
    name='create',
    version='1.0',
    py_modules=['create'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        create=create:cli
    ''',
)
