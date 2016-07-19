from setuptools import setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='learning_python',
    version='0.0.1',
    description='Simple python project',
    long_description=readme,
    author='Jaelson Carvalho',
    author_email='jaelsonjunior99@gmail.com',
    url='https://github.com/jcarva',
    license=license,
    install_requires=[
        'requests',
    ],
    )
