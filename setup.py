from setuptools import setup

setup(
   name='meshpy',
   version='1.0',
   description='Open-source Python library for generating CFD meshes',
   author='Afshawn Lotfi',
   author_email='py4m9yghi3a9@opayq.com',
   packages=['meshpy', 'meshpy.utils', 'meshpy.generators'],
   install_requires=['numpy'],
)