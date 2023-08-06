from setuptools import setup, find_packages


# see https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use

setup(name='pycvi',
      version='0.0.3',
      description='Easily compute clustering cliterions',
      url='',
      author='Yohan Foucade',
      author_email='foucade@lipn.fr',
      license='MIT',
      packages=['pycvi'],
      zip_safe=False,
      install_requires=['numpy', 'pandas'])
