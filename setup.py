from setuptools import setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python_learn',
    version='1.0.0',
    description='Simple example of python project',
    long_description=readme,
    author='Jaelson Carvalho',
    author_email='jaelsonjunior99@gmail.com',
    url='https://github.com/jcarva',
    license=license
)