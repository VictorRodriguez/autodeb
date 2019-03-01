from distutils.core import setup

setup(name='autodeb',
      version='1.0',
      description='Tool to help the creation of deb files in a clean env',
      author='Victor Rodriguez',
      author_email='vm.rod25@gmail.com',
      packages =['autodeb'],
      scripts=['autodeb/autodeb'],
      )

