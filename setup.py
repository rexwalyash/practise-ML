from setuptools import setup, find_packages
from typing import List

Hypen_E_Dot='-e .'

def get_packages(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
    if Hypen_E_Dot in requirements:
        requirements.remove(Hypen_E_Dot)

setup(
    name='ML Prediction Project',
    author="Yash Rexwal",
    author_email='rexwalyash24@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_packages('requirements.txt')
    
)