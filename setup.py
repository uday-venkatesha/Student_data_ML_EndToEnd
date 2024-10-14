from setuptools import find_packages, setup
from typing import List

hyphem_e_dot= '-e .'
def get_requirements(file_path: str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements =[req.replace('\n', '') for req in requirements]
        if hyphem_e_dot in requirement:
            requirements.remove(hyphem_e_dot)
            
        

setup(
    name = 'MLprojects',
    version= '0.0.1',
    author='Uday',
    author_email='udayvenkatesh2015@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')    
)
    