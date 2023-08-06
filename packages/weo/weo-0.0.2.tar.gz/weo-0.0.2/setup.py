# https://docs.python.org/3/distutils/setupscript.html

from setuptools import setup, find_packages
from pathlib import Path

with open('README.md', encoding='utf-8') as file:
  readme_str = '\n'.join(file.readlines())

setup(name='weo',
      version='0.0.2',
      description='Python client to read IMF WEO dataset as pandas dataframe',
      url='http://github.com/epogrebnyak/weo-reader',
      author='Evgeniy Pogrebnyak',
      author_email='e.pogrebnyak@gmail.com',
      license='MIT',
      scripts=['weo.py'],
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      long_description = readme_str,
      long_description_content_type="text/markdown",
      zip_safe=False,       
      install_requires=[
        #"requests",
        "pandas",
        #"tqdm",
        "numpy",
        "matplotlib"
        ],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Financial and Insurance Industry",  
        "Topic :: Office/Business :: Financial"
      ]
      )
