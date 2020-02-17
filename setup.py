from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='fracdiff',
      version='0.1.1',
      description='Fractional Difference for Time Series',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/ulf1/fracdiff',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['fracdiff'],
      install_requires=[
          'setuptools>=40.0.0',
          'nose>=1.3.7',
          'numpy>=1.17.1',
          'scikit-learn>=0.21.3'],
      python_requires='>=3.5',
      zip_safe=False)
