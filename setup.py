from setuptools import find_packages,setup
from typing import list

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> list[str]:

    '''  
        This function will returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file.obj:
        requirements = file.obj.readlines()
        requirements = [req.replace("\n","") for req in requirements ]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements
setup(
    name = "MLproject",
    version = "0.0.1",
    author = "Hansaka Perera",
    author_email = "whansakaperera@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')



)
