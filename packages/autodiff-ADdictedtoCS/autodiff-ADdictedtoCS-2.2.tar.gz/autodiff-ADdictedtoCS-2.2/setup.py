import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
name = 'autodiff-ADdictedtoCS',
version = '2.2',      
license='MIT',       
description = 'Automatic Differentiation Package', 
long_description=long_description,
long_description_content_type="text/markdown",
author = 'DAIKI INA',                   
author_email = 'dina@hsph.harvard.edu',      
url = 'https://github.com/ADdictedtoCS/cs207-FinalProject',   
packages = setuptools.find_packages(),
keywords = ['automatic differentiation', 'forward mode', 'reverse mode', 'optimizer'],  
install_requires=[          
          'numpy',
          'matplotlib',
      ],
classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
