from distutils.core import setup
from setuptools import find_packages
from droopssnowflake.__init__ import VERSION

setup(name='droops-snowflake',
      version=VERSION,
      description='Snowflake generator.',
      author='JohnyTheCarrot',
      author_email='johnythecarrot@gmail.com',
      url='https://github.com/JohnyTheCarrot/snowflake',
      packages=find_packages()
)
