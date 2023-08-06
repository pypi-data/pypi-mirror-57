from setuptools import setup, find_packages

setup(
    name='LaplaceDiff',
    version='0.0.2',
    author='TeamLaplace',
    author_email='yanlitao@outlook.com',
    description='automatic differentiation',
    url='https://github.com/Team-Laplace/cs207-FinalProject/tree/master/LaplaceDiff',
    packages=find_packages(exclude=('LaplaceDiff/UnitTests',)),
    install_requires=['numpy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
