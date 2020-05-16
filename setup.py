from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='numpy-fracdiff',
      version='0.3.1',
      description='Fractional Difference for Time Series',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/ulf1/numpy-fracdiff',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['numpy_fracdiff'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.18.*',
          'numba>=0.48.*'],
      python_requires='>=3.6',
      zip_safe=False)
