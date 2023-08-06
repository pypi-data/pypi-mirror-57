from setuptools import setup, find_packages
from pathlib import Path

# 0.0.2 changes folder storage to ~/.boo and exposes file location helpers 
#       raw_filepath(year) and processed_filepath(year)

# 0.0.3 migrates client to http://github.com/ru-corporate/boo 
#       and makes it minimalistic, column naming is similar to csvcut,
#       filtering done via pandas  

# 0.0.4 adds wipe() and wipe_all() functions

# 0.0.5 README will surface on PyPi

# 0.0.6 additional dataset cleaning moved from notebook to package

# 0.0.7 help messages and whatis() function

# 0.0.8 more tests 

# 0.0.9 large_companies() imported at root

# 0.0.91 okved import changed

# 0.1.0 year 2018 added

# See 

with open('README.md', encoding='utf-8') as file:
  readme_str = '\n'.join(file.readlines())

setup(name='boo',
      version='0.1.0',
      description='Russian corporate reports 2012-2018',
      url='http://github.com/ru-corporate/boo',
      author='Evgeniy Pogrebnyak',
      author_email='e.pogrebnyak@gmail.com',
      license='MIT',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      long_description = readme_str,
      long_description_content_type="text/markdown",
      zip_safe=False, 
      install_requires=[
        "requests",
        "pandas",
        "tqdm"
        ],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Financial and Insurance Industry",  
        "Topic :: Office/Business :: Financial",    
        "Topic :: Utilities"
      ]
      )
