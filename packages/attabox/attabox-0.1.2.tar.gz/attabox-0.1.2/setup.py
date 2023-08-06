from setuptools import setup

setup(name='attabox',
      version='0.1.2',
      description='Attali Utility Library',
      url='http://github.com/',
      author='Poidudes',
      author_email='yonatan.attali@gmail.com',
      license='MIT',
      packages=['attabox'],
      install_requires=[
          'matplotlib',
      ],
      zip_safe=False)