from distutils.core import setup

setup(name='mavr_module',
      version='0.0.3',
      description='SubModules for MAVR SAO RAN',
      author='Anatoly Beskakotov',
      author_email='beskakotov.as@gmail.com',
      url='https://github.com/Black13Wolf/mavr_module',
      packages=['mavr',],
      install_requires=['numpy', 'astropy'],
     )