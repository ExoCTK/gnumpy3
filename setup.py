try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='gnumpy',
      version='0.2',
      description="Gnumpy is a simple Python module that interfaces in a way "
      "almost identical to numpy, but does its computations on your "
      "computer's  GPU, using Cudamat.",
      author='Tijmen Tieleman',
      license='BSD-derived (see LICENSE)',
      url='http://www.cs.toronto.edu/~tijmen/gnumpy.html',
      )