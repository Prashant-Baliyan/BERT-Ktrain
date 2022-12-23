from setuptools import find_packages, setup
from typing import List


def get_requirements_list()-> List[str]:
    
    """
    Description: This function is going to return list of requirement mention in requirement.txt file.
    Retuen this function is going to return a list which contain name of libraries mention in requirement.txt file.
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_file.readlines().remove("-e .")

#Declaring variable for setup function
PROJECTNAME = "BERT-Ktrain"
VERSION = "0.0.3"
AUTHOR = "Prashant Baliyan"
DESCRIPTION = "BERT-Ktrain"
PACKAGES = "src"
REQUIREMENTS_FILE_NAME = 'requirements.txt'

setup(
name = PROJECTNAME,
version= VERSION,
author= AUTHOR,
description= DESCRIPTION,
packages= find_packages(),
install_requires = get_requirements_list()
)