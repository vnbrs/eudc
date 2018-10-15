from setuptools import setup

setup(
    name="udce",
    description="""
        A CLI tool that helps you to find and exterminatate unnecessary debugging calls on your code such as `console.log`, `byebug` and so on.
    """,
    url="https://github.com/vnbrs/udce",
    version="1.0",
    author="Vinicius Brasil",
    author_email="vnbrs@icloud.com",
    packages=["eudc"],
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        udce=udce:cli
    """,
)
