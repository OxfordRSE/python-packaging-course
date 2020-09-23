from setuptools import setup

setup(name='tstools',
      version='0.1',
      description='A package to analyse timeseries',
      url='',
      author='Spam Eggs',
      author_email='spameggs@example.com',
      packages=['tstools'],
      package_data={"tstools": ["test_data/*"]},
      install_requires = ["numpy", "matplotlib"],
      license='GPLv3')
