from setuptools import setup

MAJOR = 0
MINOR = 0
MICRO = 3

version = f'{MAJOR}.{MINOR}.{MICRO}'

setup(
    name='QualitativeModelFitting',
    version=version,
    packages=['qualitative_model_fitting'],
    license='MIT',
    long_description='package for unit testing sbml models',
    author='Ciaran Welsh',
    author_email='ciaran.welsh@newcastle.ac.uk',
    url='https://github.com/CiaranWelsh/QualitativeModelFitting',
    keywords=['SBML', 'antimony', 'tellurium', 'qualitative modelling'],
    install_requires=open('requirements.txt').readlines()
)
