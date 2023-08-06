from setuptools import setup

setup(name='kcman',
      version='0.1',
      description='Aeropost manager for DEV, STAGE and PROD environments',
      author='Juan Diego Vega Corella',
      author_email='jdvega@aeropost.com',
      license='MIT',
      packages=['kcman'],
      scripts=['bin/kcman'],
      install_requires=[
          'questionary',
      ],
      zip_safe=False)