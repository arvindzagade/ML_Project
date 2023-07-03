"""
  setup.py file will be responsible in creating ML application as a package and even deploy in pypi
  setup file will find all the packeges required
  we will be createing src folder where __init__ is mentioned and will read all the folders
   where we have used __init__.py and it will take all those packages

"""

from setuptools import find_packages,setup  # will find all the packages in our directory.
from typing import List

HYPEN_E_DOT = '-e .' 

## our -e . in requirement file will connect to setup file. but this should not be consider if we import
## packages from requirement.txt, so we are writing a condition that our setup file will not read that -e .

def get_requirements(file_path:str) -> List[str]:
    """
    This function will return the list of requirements that we need to install for project
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() ## reading the lines
        requirements = [req.replace("\n","") for req in requirements]#we are removing /n when we are moving to next line in req file
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

## this is metadata about entire project in setup below.
setup(
    name="ML_Project",
    version="0.0.1",
    author="Arvind",
    author_email="arvindzagade@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    
    )