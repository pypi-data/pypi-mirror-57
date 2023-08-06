from setuptools import setup, find_packages

setup(
    name='LaplaceDiff',
    version='0.0.1',
    author='TeamLaplace',
    author_email='yanlitao@outlook.com',
    description='automatic differentiation',
    packages=find_packages(exclude=('UnitTests',)),
    install_requires=['numpy'],
)
