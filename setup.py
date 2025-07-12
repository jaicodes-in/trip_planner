from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()

                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except Exception as e:
        print(e)

    return requirement_list

print(get_requirements())    
setup(
    author="Jai-Panchal",
    author_email="jaipanchal97@gmail.com",
    packages=find_packages(),
    name="AI-PLANNER-AGENT",
    version="0.0.1",
    install_requires=get_requirements()
    
)