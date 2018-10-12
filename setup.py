from setuptools import setup

setup(
    name='udce',
    version='1.0',
    py_modules='udce',
    install_requires=['Click',],
    entry_points='''
        [console_scripts]
        udce=udce:cli
    ''',
)
