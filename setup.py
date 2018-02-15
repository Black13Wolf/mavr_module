#from distutils.core import setup
from setuptools import setup
from mavr import __version__
setup(name='mavr_module',
      version=__version__,
      description='SubModules for MAVR SAO RAN',
      author='Anatoly Beskakotov',
      author_email='beskakotov.as@gmail.com',
      url='https://github.com/Black13Wolf/mavr_module',
      packages=['mavr',],
      install_requires=['numpy', 'astropy', 'matplotlib'],
     )