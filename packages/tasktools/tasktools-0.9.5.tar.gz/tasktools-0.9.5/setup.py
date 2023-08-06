from setuptools import setup, find_packages
from networktools.requeriments import read

setup(name='tasktools',
      version='0.9.5',
      description='Some useful tools for asycnio Tasks: async while, the Scheduler and Assignator classes',
      url='https://tasktools.readthedocs.io/en/latest/',
      author='David Pineda Osorio',
      author_email='dpineda@uchile.cl',
      license='GPL3',
      install_requires=find_packages(),
      packages=['tasktools', ],
      package_dir={'tasktools': 'tasktools'},
      package_data={
          'tasktools': ['../doc', '../docs', '../requeriments.txt']},
      zip_safe=False)
